from objects.base import BaseObject
from objects.texts import RecalculableText
import pygame


class IllegalTableArgumentException(Exception):
    pass


class HighscoreTableRow:
    player_name: str
    player_score: int
    name_text: RecalculableText
    score_text: RecalculableText
    x: int
    y: int
    insets: int
    column_size: int

    def __init__(self,
                 player_data: dict,
                 x: int,
                 y: int,
                 insets: int = 5,
                 size: int = 16,
                 left_color: pygame.Color = pygame.Color(230, 230, 0),
                 right_color: pygame.Color = pygame.Color(0, 230, 230),
                 column_size: int = 120
                 ):
        self.x = x
        self.y = y
        self.player_name = str(player_data["name"])
        if not isinstance(player_data["score"], int):
            raise IllegalTableArgumentException("Field score is not an int")
        self.player_score = player_data["score"]
        self.insets = insets
        self.column_size = column_size
        self.name_text = RecalculableText(
            x + insets,
            y + insets,
            self.player_name,
            size,
            left_color
        )
        self.score_text = RecalculableText(
            column_size + x + insets,
            y + insets,
            str(self.player_score),
            size,
            right_color
        )

    def draw(self, screen):
        self.score_text.draw(screen)
        self.name_text.draw(screen)

    def draw_at(self, screen, x: int, y: int):
        old_score_x, old_score_y = self.score_text.rect.x, self.score_text.rect.y
        old_name_x, old_name_y = self.name_text.rect.x, self.name_text.rect.y
        self.name_text.rect.x = x + self.insets
        self.name_text.rect.y = y + self.insets
        self.score_text.rect.x = x + self.column_size + self.insets
        self.score_text.rect.y = y + self.insets
        self.draw(screen)
        self.name_text.rect.x, self.name_text.rect.y = old_name_x, old_name_y
        self.score_text.rect.x, self.score_text.rect.y = old_score_x, old_score_y

    def move(self, dx, dy):
        self.name_text.rect.x += dx
        self.score_text.rect.x += dx
        self.name_text.rect.y += dy
        self.score_text.rect.y += dy


class HighscoreTableDrawer(BaseObject):
    application = None

    """
    Creates a highscore table

    x: x position on the screen
    y: y position on the screen
    scores: list of dict {"name": str, "score": int}
            highscores
    cell_insets: padding from cell borders
    text_size: size of cells' text
    left_color: color of "name" column
    right_color: color of "score" column
    column_size: size of one column in pixels
    max_display_lines: 
        when set to -1 (default):
            displays all table rows at once
        when set to >0:
            limits number of rows displayed at once.
            if number of rows > max_display_lines,
            scrolling enables
    """

    def __init__(
            self,
            x: int,
            y: int,
            scores: list[dict],
            cell_insets: int = 5,
            text_size: int = 16,
            left_color: pygame.Color = pygame.Color(230, 230, 0),
            right_color: pygame.Color = pygame.Color(0, 230, 230),
            column_size: int = 120,
            max_display_lines: int = -1
    ):
        super().__init__(
            x,
            y,
            cell_insets * 4 + column_size * 2,
            (text_size + cell_insets * 2) * (len(scores) if max_display_lines == -1 else max_display_lines)
        )
        self.rows: list[HighscoreTableRow] = []
        self.current_scroll = 0
        self.line_display_count = -1
        self.text_size = text_size
        self.cell_insets = cell_insets
        self.scores = scores
        if max_display_lines == 0:
            raise IllegalTableArgumentException("max_display_lines can be only -1 or integer > 0")
        self.line_display_count = max_display_lines
        for pos, score in enumerate(self.scores):
            self.rows.append(HighscoreTableRow(
                score,
                x,
                y + pos * (text_size + cell_insets * 2),
                cell_insets,
                text_size,
                left_color,
                right_color,
                column_size
            ))

    def event(self, event):
        super().event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*HighscoreTableDrawer.application.shrink_scaled_pos(pygame.mouse.get_pos())):
                if event.button == 4:
                    self.current_scroll = self.current_scroll - 1 if self.current_scroll > 0 else 0
                elif event.button == 5:
                    self.current_scroll = self.current_scroll + 1 \
                        if self.current_scroll + self.line_display_count < len(self.rows) \
                        else self.current_scroll

    def draw(self, screen):
        super().draw(screen)
        if len(self.rows) < 1:
            return
        if self.line_display_count == -1:
            for row in self.rows:
                row.draw(screen)
        else:
            for line_no in range(self.current_scroll, self.line_display_count + self.current_scroll):
                if line_no >= len(self.rows):
                    break
                self.rows[line_no].draw_at(
                    screen,
                    self.rect.x,
                    self.rect.y + (line_no - self.current_scroll) * (self.text_size + self.cell_insets * 2)
                )
            one_line_scroll_bar_height = self.rect.height // len(self.rows)
            resulting_scroll_bar_height = one_line_scroll_bar_height * self.line_display_count
            scroll_bar_y = one_line_scroll_bar_height * self.current_scroll
            pygame.draw.rect(screen, pygame.Color("gray"), (self.rect.x + self.rect.width,
                                                            self.rect.y + scroll_bar_y,
                                                            4,
                                                            resulting_scroll_bar_height))

    def move_to(self, nx, ny):
        dx, dy = nx - self.rect.x, ny - self.rect.y
        self.rect.x = nx
        self.rect.y = ny
        for row in range(len(self.rows)):
            self.rows[row].move(dx, dy)