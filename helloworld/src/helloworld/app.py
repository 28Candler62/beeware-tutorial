"""
My first application
"""
from . import confmethods

import toga
from toga.style import Pack

class HelloWorld(toga.App):
    def startup(self):
        self.main_name_input = toga.TextInput(style=Pack(flex=1))
        self.main_display_input = toga.TextInput(style=Pack(flex=1), readonly=True)
        self.setup_in_file_name_input = toga.TextInput(value='(location number)-mm-dd-yyyy.pdf',readonly=True, style=Pack(flex=1))
        self.setup_in_file_folder_input = toga.TextInput(readonly=True, style=Pack(flex=1), id='in_file_folder_input')
        self.setup_out_file_name_input = toga.TextInput(value='import-mm-dd-yyyy.csv',readonly=True, style=Pack(flex=1))
        self.setup_out_file_folder_input = toga.TextInput(readonly=True, style=Pack(flex=1), id='out_file_folder_input')
        self.setup_out_file_date_input = toga.TextInput(value='(Report Date)',readonly=True, style=Pack(flex=1))
        self.setup_out_file_reference_input = toga.TextInput(value='(Location number) yyyy',readonly=True, style=Pack(flex=1))
        self.setup_out_file_jobid_input = toga.TextInput(value='(Location number)',readonly=True, style=Pack(flex=1))
        self.location_edit_input = toga.TextInput(style=Pack(flex=1))
        self.location_table = toga.Table(headings=['Location Numbers'], style=Pack(padding=5), data=confmethods.get_locations())
        self.accounts_table = toga.Table(
            headings=['Required', 'Acct ID', 'ID Only', 'Description', 'Debit', 'Credit', 'Report', 'Table', 'Row', 'Field'],
            style=Pack(padding=5),
            data=[
                
            ]
        )

        #   Main
        self.main_box = toga.Box(id='main_box', style=Pack(direction='column'), children=[
            toga.Box(id='name_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Your name: ",style=Pack(padding=(0, 5))),
                    self.main_name_input 
                ]),
            toga.Box(id='display_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label('Display Here: ', style=Pack(padding=(0, 5))),
                    self.main_display_input
                ]),
            toga.Button("Say Hello!", on_press=self.say_hello, style=Pack(padding=5))
            ]
        )

        # Setup Files
        self.setup_box = toga.Box(id='setup_box', style=Pack(direction='column'), children=[
            toga.Label("Input Pulse report files: ", style=Pack(padding=(0, 5), flex=1)),
            toga.Box(id='in_file_name_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Pulse file name: ", style=Pack(padding=(0, 5))),
                    self.setup_in_file_name_input,
                    toga.Label("Example: 1234-12-25-2024.pdf ", style=Pack(padding=(0, 5)))
                ]),
            toga.Box(id='in_file_folder_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Folder location: ", style=Pack(padding=(0, 5))),
                    self.setup_in_file_folder_input,
                    toga.Button("Select Folder", on_press=self.select_folder_text_input('in_file_folder_input'), style=Pack(padding=5))
                ]),
            toga.Divider(style=Pack(background_color='white')),
            toga.Label("SAGE Import CSV file: ", style=Pack(padding=(5), flex=1)),
            toga.Box(id='out_file_name_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("SAGE file name: ", style=Pack(padding=(0, 5))),
                    self.setup_out_file_name_input,
                    toga.Label("Example: import-12-25-2024.csv", style=Pack(padding=(0, 5)))
                ]),
            toga.Box(id='out_file_folder_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Folder location: ", style=Pack(padding=(0, 5))),
                    self.setup_out_file_folder_input,
                    toga.Button("Select Folder", on_press=self.select_folder_text_input('out_file_folder_input'), style=Pack(padding=5))
                ]),
            toga.Box(id='out_file_date_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Date: ", style=Pack(padding=(0, 5))),
                    self.setup_out_file_date_input,
                    toga.Label("Example: 2/26/2024", style=Pack(padding=(0, 5)))
                ]),
            toga.Box(id='out_file_account_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Account ID: ", style=Pack(padding=(0, 5))),
                    toga.Label("Refer to Account List Configuration", style=Pack(padding=(0, 5)))
                ]),
            toga.Box(id='out_file_reference_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Reference: ", style=Pack(padding=(0, 5))),
                    self.setup_out_file_reference_input,
                    toga.Label("Exanple: 1234 2024", style=Pack(padding=(0, 5)))
                ]),
            toga.Box(id='out_file_jobid_box', style=Pack(direction='row', padding=5),
                children=[
                    toga.Label("Job ID: ", style=Pack(padding=(0, 5))),
                    self.setup_out_file_jobid_input,
                    toga.Label("Example: 1234", style=Pack(padding=(0, 5)))
                ])
            ]
        )

        #   Accounts Listing Edit box
        self.accounts_edit_box = toga.Box(id='accounts_listing_edit_box', style=Pack(direction='column', width=100), children=[
            toga.Switch('required', style=Pack(padding=5)),
            toga.TextInput(style=Pack(padding=5)),
            toga.Switch('id only', style=Pack(padding=5)),
            toga.TextInput(style=Pack(padding=5)),
            toga.Switch('debit', style=Pack(padding=5)),
            toga.Switch('credit', style=Pack(padding=5)),
            toga.Selection(style=Pack(padding=5)),
            toga.Selection(style=Pack(padding=5)),
            toga.Selection(style=Pack(padding=5)),
            toga.Selection(style=Pack(padding=5)),
            toga.Button('Save', on_press=self.accounts_edit_close_self)
        ])

        #   Accounts listing Setup Page
        self.accounts_box = toga.Box(id='accounts_box', style=Pack(direction='column'), children=[
            toga.Button('Add Row', id='accounts_add_row_btn', on_press=self.accounts_self_insert, style=Pack(padding=5)),
            self.accounts_table,
        ])

        #   Locations Page
        self.locations_box = toga.SplitContainer(id='locations_box', style=Pack(direction='column'), content=[
            toga.Box(id="location_edit", style=Pack(direction='column'), children=[
                toga.Label("Location: ", style=Pack(padding=(0, 5))),
                self.location_edit_input,
                toga.Button("Add/Update", id='locations_add_update_btn',on_press=self.location_add_update, style=Pack(padding=5)),
                toga.Button("Edit", id='locations_edit_btn', on_press=self.location_edit, style=Pack(padding=5)),
                toga.Button("Remove", id='locations_remove_btn', on_press=self.location_remove, style=Pack(padding=5))
                ]),
                self.location_table
            ]
        )

        #   Registration Page
        registration_box = toga.Box(style=Pack(direction='column'), id='setup_box')
        self.get_registration = registration_box
        
        #   COMMANDS
        cmd0 = toga.Command(text='Main', action=self.switch_content_box, tooltip='Go to Main Page', order=0)
        cmd1 = toga.Command(text='File Setup', action=self.switch_content_box, tooltip='Go to Setup Page', order=1)
        cmd2 = toga.Command(text='Accounts Setup', action=self.switch_content_box, tooltip='Go to Accounts Setup Page', order=2)
        cmd3 = toga.Command(text='Locations', action=self.switch_content_box, tooltip='Go to Locations Page', order=3)
        cmd4 = toga.Command(text='Registration', action=self.switch_content_box, tooltip='Go to Registration Page',order=4)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.toolbar.add(cmd0, cmd1, cmd2, cmd3, cmd4)
        self.main_window.content = self.main_box
        self.main_window.show()

        self.content_boxes = {
            'Main': self.main_box,
            'File Setup': self.setup_box,
            'Accounts Setup': self.accounts_box,
            'Locations': self.locations_box,
            'Registration': self.get_registration
        }

    def say_hello(self, widget):
        self.main_display_input.value = self.main_name_input.value

    def switch_content_box(self, widget):
        self.main_window.content = self.content_boxes[widget.text]
    
    def disp_dialog(self, ttle, msg):
        self.main_window.info_dialog(
            ttle, msg
        )

    def select_folder_text_input(self, arg1):
        async def select_folder_text_input(self):
            self = self.app
            folder = await self.main_window.select_folder_dialog('Select Folder')
            self.widgets[arg1].value = folder
        return select_folder_text_input
    
    def accounts_self_insert(self, widget):
        self.accounts_table.data.append((
            self.accounts_edit_box.children[0].value,
            self.accounts_edit_box.children[1].value,
            self.accounts_edit_box.children[2].value,
            self.accounts_edit_box.children[3].value,
            self.accounts_edit_box.children[4].value,
            self.accounts_edit_box.children[5].value,
            self.accounts_edit_box.children[6].value,
            self.accounts_edit_box.children[7].value,
            self.accounts_edit_box.children[8].value,
            self.accounts_edit_box.children[9].value
        ))        
        self.main_window.widgets['accounts_add_row_btn'].style.visibility = 'hidden'
        widget.parent.insert(0, self.accounts_edit_box)
        # print(widget.parent.children.index(widget))
        # self.accounts_box.refresh()

    def accounts_edit_close_self(self, widget):
        self.main_window.widgets['accounts_add_row_btn'].style.visibility = 'visible'
        self.accounts_table.data.__delitem__(-1)
        widget.parent.parent.remove(widget.parent)
    
    def location_add_update(self, widget):
        try:
            new_int = int(self.location_edit_input.value)
        except ValueError:
            self.disp_dialog('Value Error', f"Could not convert\n\n'{self.location_edit_input.value}'\n\n to an integer.")
            return
        t_set = set(r.location_numbers for r in self.location_table.data)
        t_set.add(new_int)
        t_set = sorted(t_set)
        self.location_table.data = confmethods.set_locations(t_set)
        self.location_edit_input.value = None

    async def location_remove(self, widget):
        try:
            if await self.main_window.confirm_dialog(f"Remove: '{self.location_table.selection.location_numbers}' ?", 'Press "OK" to continue.'):
                self.location_table.data = confmethods.remove_location(self.location_table.selection.location_numbers)
        except AttributeError:
            self.disp_dialog('No Location Selected!', 'Select Location number BEFORE clicking "Remove"')
    
    def location_edit_save(self, widget):
        self.location_table.data = confmethods.remove_location(self.location_table.selection.location_numbers)
        self.location_add_update(widget)
        widget.parent.remove(self.main_window.widgets['locations_edit_save_btn'])
        self.main_window.widgets['locations_add_update_btn'].style.visibility = 'visible'
        self.main_window.widgets['locations_edit_btn'].style.visibility = 'visible'
        self.main_window.widgets['locations_remove_btn'].style.visibility = 'visible'

    async def location_edit(self, widget): 
        try:
            if await self.main_window.confirm_dialog(f"Edit: '{self.location_table.selection.location_numbers}' ?", 'After editing, click "Save" to save.".'):
                self.location_edit_input.value = self.location_table.selection.location_numbers
                self.main_window.widgets['locations_add_update_btn'].style.visibility = 'hidden'
                self.main_window.widgets['locations_edit_btn'].style.visibility = 'hidden'
                self.main_window.widgets['locations_remove_btn'].style.visibility = 'hidden'
                widget.parent.add(toga.Button('Save', id='locations_edit_save_btn', on_press=self.location_edit_save, style=Pack(padding=5)))
        except AttributeError:
            self.disp_dialog('No Location Selected!', 'Select Location number BEFORE clicking "Edit"')

def main():
    return HelloWorld()