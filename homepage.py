import customtkinter 




class ClassName(customtkinter.CTk):
	"""docstring for ClassName"""

	customtkinter.set_appearance_mode('dark')
	
	def __init__(self, *args):
		super(*args).__init__()


		""" Your stuffs here"""








def main():
	mm = customtkinter.CTk()
	mm = ClassName()
	mm.geometry('500x500')
	mm.mainloop()

if __name__ == "__main__":
	app = main()