import random

import pygame as pg
from pygame.locals import *


class BubbleSort:
    FPS = 200
    WIDTH, HEIGHT = 1280, 480
    BAR_WIDTH, BAR_HEIGHT = 10, 15

    unordered_list = []

    is_sorted = False
    is_running = True

    def bubble_sort(self) -> bool:
        ordered = 0

        while True:
            swaps = 0
            for i in range((len(self.unordered_list) - 1) - ordered):
                if self.unordered_list[i] > self.unordered_list[i + 1]:
                    self.unordered_list[i], self.unordered_list[i + 1] = (
                        self.unordered_list[i + 1],
                        self.unordered_list[i],
                    )
                    swaps += 1

                self.draw_bars(active=(i, i + 1))
            ordered += 1

            if swaps == 0:
                self.is_sorted = True
                return

    def random_list(self) -> None:
        return [random.randint(0, 20) for _ in range(self.WIDTH // self.BAR_WIDTH)]

    def draw_bars(self, active: tuple = None) -> None:
        active = active or tuple()

        # Clear the screen
        self.surface.fill((0, 0, 0))

        # Displays the bars
        for i, v in enumerate(self.unordered_list):
            pg.draw.rect(
                surface=self.surface,
                color=(0, 255, 0) if i in active else (255, 255, 255),
                rect=(
                    i * self.BAR_WIDTH,
                    self.HEIGHT - v * self.BAR_HEIGHT,
                    self.BAR_WIDTH,
                    v * self.BAR_HEIGHT,
                ),
            )

        # Updates the screen
        pg.display.update()

        # Tick
        self.clock.tick(self.FPS)

    def update(self) -> None:
        if not self.is_sorted:
            self.bubble_sort()

    def run(self) -> None:
        pg.init()

        self.clock = pg.time.Clock()
        self.surface = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("Bubble Sort")

        self.unordered_list = self.random_list()

        # Update screen
        while self.is_running:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.is_running = False

            self.update()


def main() -> None:
    BubbleSort().run()


if __name__ == "__main__":
    main()
