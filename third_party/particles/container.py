from .base import Particle


class ParticleContainer:
    def __init__(self, *args):
        self.particles = [particle.copy() for particle in args]

    def __len__(self):
        return len(self.particles)

    def __getitem__(self, item: int):
        return self.particles[item]

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
        self.particles = [particle for particle in self.particles if particle.is_alive()]

    def append(self, particle: Particle):
        self.particles.append(particle.copy())
