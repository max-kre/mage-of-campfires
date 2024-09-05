import pygame, sys
from bin.settings import GAMEVERSION


class MainMenu:
	def __init__(self) -> None:
		# initialise pygame
		pygame.init()
		# run menu 
		self.menu_runs = True
		# set menu background
		self.display_surface = pygame.display.get_surface()
		self.bg_menu = pygame.image.load('data/graphics/menu.png')
		self.clock = pygame.time.Clock()
		
		self.button1 = Button('New Game',200,40,(25,50),5)
		self.button2 = Button('Highscore',200,40,(25,150),5)
		self.button3 = Button('Options',200,40,(25,250),5)
		self.button4 = Button('Exit Game',200,40,(25,720),5)
		self.base_font = pygame.font.Font(None,20)
		self.text_surf = self.base_font.render("V"+str(GAMEVERSION),True,'#faf78d')


	def run(self):
		dt = self.clock.tick() / 1000
		while self.menu_runs == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("I wanna quit menu")
					pygame.quit()
					sys.exit()
			self.update()
			pygame.display.update()
			#print("menu is running")
		return

	def update(self):

		self.display_surface.blit(self.bg_menu,(0,0))
		self.button1.draw()
		self.button2.draw()
		self.button3.draw()
		self.button4.draw()
		self.display_surface.blit(self.text_surf,(1130,775))



		if self.button1.check_click() == True:
			self.menu_runs = False
			return (False)

		if self.button4.check_click() == True:
			pygame.quit()
			sys.exit()
		
		else:
			return(True)

		pygame.display.update()

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
		self.gui_font = pygame.font.Font(None,30)
		self.display_surface = pygame.display.get_surface()

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#3e0d19'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#1b0611'
		#text
		self.text_surf = self.gui_font.render(text,True,'#faf78d')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(self.display_surface,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(self.display_surface,self.top_color, self.top_rect,border_radius = 12)
		self.display_surface.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				return(True)
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
					return(False)
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#841924'
			
	#def quit(self):
	#    print("quit")