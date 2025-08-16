import os
import sys
import time
import math
import random
from argparse import ArgumentParser
from colorama import Fore, Style
from itertools import cycle

class AdvancedASCIIAnimator:
    def __init__(self, frames=None, delay=0.05, effect='vortex', color_mode='rainbow'):
        self.frames = frames or []
        self.delay = delay
        self.effect = effect
        self.color_cycle = cycle([
            Fore.RED, Fore.GREEN, Fore.YELLOW, 
            Fore.BLUE, Fore.MAGENTA, Fore.CYAN
        ])
        self.particles = []
        
        # 特效参数配置
        self.effect_config = {
            'vortex': {'speed': 0.3, 'radius_growth': 0.2},
            'particle': {'max_particles': 50, 'spawn_rate': 3},
            'matrix': {'density': 0.08, 'fade_speed': 0.9}
        }

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.frames = [frame.strip() for frame in f.read().split('\n\n')]

    def add_frame(self, frame):
        self.frames.append(frame)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def apply_vortex(self, frame, tick):
        lines = frame.split('\n')
        max_width = max(len(line) for line in lines)
        max_height = len(lines)
        result = []
        
        center_x = max_width / 2
        center_y = max_height / 2
        angle = tick * self.effect_config['vortex']['speed']
        
        for y, line in enumerate(lines):
            new_line = []
            for x, char in enumerate(line.ljust(max_width)):
                # 极坐标变换
                dx = x - center_x
                dy = y - center_y
                distance = math.hypot(dx, dy)
                radius = distance * self.effect_config['vortex']['radius_growth']
                
                theta = math.atan2(dy, dx) + angle
                new_x = int(center_x + radius * math.cos(theta))
                new_y = int(center_y + radius * math.sin(theta))
                
                if 0 <= new_x < max_width and 0 <= new_y < max_height:
                    new_char = lines[new_y][new_x] if new_x < len(lines[new_y]) else ' '
                else:
                    new_char = ' '
                
                color = self.get_color(distance, max_width, tick)
                new_line.append(color + new_char)
            result.append(''.join(new_line))
        return '\n'.join(result)

    def apply_particle(self, frame, tick):
        # 粒子生成逻辑
        if len(self.particles) < self.effect_config['particle']['max_particles']:
            if random.random() < self.effect_config['particle']['spawn_rate'] / 100:
                self.particles.append({
                    'x': random.randint(0, 50),
                    'y': 0,
                    'vx': random.uniform(-0.5, 0.5),
                    'vy': random.uniform(0.5, 1.5),
                    'life': 1.0
                })
        
        # 更新粒子状态
        new_frame = []
        for line in frame.split('\n'):
            new_frame.append(list(line.ljust(50)))
        
        for p in self.particles:
            if p['life'] <= 0:
                continue
            x = int(p['x'])
            y = int(p['y'])
            if 0 <= y < len(new_frame) and 0 <= x < len(new_frame[y]):
                new_frame[y][x] = next(self.color_cycle) + '*'
            
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['life'] -= 0.02
        
        # 移除死亡粒子
        self.particles = [p for p in self.particles if p['life'] > 0]
        return '\n'.join(''.join(line) for line in new_frame)

    def get_color(self, value, max_value, tick):
        colors = [
            Fore.RED, Fore.YELLOW, Fore.GREEN,
            Fore.CYAN, Fore.BLUE, Fore.MAGENTA
        ]
        phase = (tick % 60) / 60
        index = int((value/max_value + phase) * len(colors)) % len(colors)
        return colors[index]

    def run(self):
        try:
            tick = 0
            while True:
                for frame in self.frames:
                    self.clear_screen()
                    
                    if self.effect == 'vortex':
                        processed = self.apply_vortex(frame, tick)
                    elif self.effect == 'particle':
                        processed = self.apply_particle(frame, tick)
                    else:
                        processed = frame
                    
                    print(Style.RESET_ALL + processed)
                    time.sleep(self.delay)
                    tick += 1
        except KeyboardInterrupt:
            print(Style.RESET_ALL + "\nAnimation terminated.")

if __name__ == "__main__":
    parser = ArgumentParser(description="Advanced ASCII Animator")
    parser.add_argument("-f", "--file", help="Input file with ASCII frames")
    parser.add_argument("-e", "--effect", choices=['vortex', 'particle', 'matrix'], 
                       default='vortex', help="Animation effect type")
    parser.add_argument("-d", "--delay", type=float, default=0.05,
                       help="Frame delay in seconds")
    
    args = parser.parse_args()
    
    anim = AdvancedASCIIAnimator(delay=args.delay, effect=args.effect)
    
    if args.file:
        anim.load_from_file(args.file)
    else:
        # 默认示例动画
        anim.add_frame(r"""
          ____
         /    \ 
        | STOP | 
         \____/
        """)
        anim.add_frame(r"""
          ____
         /    \ 
        | GO   | 
         \____/
        """)
    
    anim.run()
