from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from data_bridge import *


class GUI_Creator_temp:
    def __init__(self):
        self.data_bridge = Singleton(Data_bridge)
        self.root = Tk()
        self.root.title("Streamix : Enhancing Video Conferencing Platforms")
        self.content = ttk.Frame(self.root, padding=(10, 10, 10, 10))
        self.chosen_method = StringVar()

    def defining_labels(self):
        # Title label
        self.title_label = ttk.Label(
            self.content, text="Video Enhancing Features")
        self.title_label.config(font=("Courier", 18, 'bold'))

        self.methods_label = ttk.Label(self.content, text="Methods")
        self.methods_label.config(font=("Courier", 12, 'bold'))

    def defining_buttons(self):
        # video select button
        self.video_select_button = ttk.Button(
            self.content, text="Select Video", command=self.select_video_file)

        # Virtual Background button
        self.bg_select_button = ttk.Button(
            self.content,
            text="Select Virtual BG",
            command=self.select_background_file)

        # process video button
        self.process_video_button = ttk.Button(
            self.content,
            text="Process frame",
            command=self.process_video_method)

        # stop video processing video button
        self.stop_video_processing_button = ttk.Button(
            self.content, text="Stop processing", command=self.stop_processing_video)

    def select_video_file(self):
        self.selected_video_file_path = filedialog.askopenfilename()
        self.data_bridge.selected_video_file_path = self.selected_video_file_path

    def select_background_file(self):
        self.selected_background_file_path = filedialog.askopenfilename()
        self.data_bridge.selected_background_file_path = self.selected_background_file_path

    def define_radio_buttons_for_method_select(self):
        self.raw_video = ttk.Radiobutton(
            self.content,
            text='Raw Video',
            variable=self.chosen_method,
            value='raw_video')
        self.virtual_bg = ttk.Radiobutton(
            self.content,
            text='Virtual Background',
            variable=self.chosen_method,
            value='virtual_bg')

    def process_video_method(self):
        self.data_bridge.methode_chosen_by_radio_butten = self.chosen_method.get()
        self.data_bridge.start_process_manager = True
        pass

    def stop_processing_video(self):
        self.data_bridge.start_process_manager = False
        pass

    def defining_geometry_grid(self):
        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        self.title_label.grid(column=1, row=0, sticky=(N, W), padx=5)
        self.raw_video.grid(column=1, row=6)
        self.virtual_bg.grid(column=1, row=7)
        self.process_video_button.grid(column=1, row=8)
        self.stop_video_processing_button.grid(column=1, row=9)
        self.video_select_button.grid(column=0, row=2)
        self.methods_label.grid(column=1, row=5, sticky=(N))
        self.bg_select_button.grid(
            column=4,
            row=2,
            columnspan=2,
            sticky=(
                N,
                W))

    def defining_whole_ui(self):
        self.defining_labels()
        self.defining_buttons()
        self.define_radio_buttons_for_method_select()
        self.defining_geometry_grid()

    def update(self):
        print("The text is", self.newname.get())
        self.root.mainloop()
