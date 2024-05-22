import wx
import wx.lib.mixins.listctrl as listmix

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "ListCtrl Example", size=(500, 300))
        panel = wx.Panel(self, wx.ID_ANY)

        # Crear el ListCtrl
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, "Column 1")
        self.list_ctrl.InsertColumn(1, "Column 2")
        self.list_ctrl.InsertColumn(2, "Column 3")
        self.list_ctrl.InsertColumn(3, "Column 4")

        # Agregar algunos elementos de ejemplo
        data = [
            ("Item 1-1", "Item 1-2", "Item 1-3", "Item 1-4"),
            ("Item 2-1", "Item 2-2", "Item 2-3", "Item 2-4"),
            ("Item 3-1", "Item 3-2", "Item 3-3", "Item 3-4")
        ]

        for row in data:
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), row[0])
            for col, item in enumerate(row[1:], start=1):
                self.list_ctrl.SetItem(index, col, item)

        # Crear un botón para obtener la lista de valores de la columna 1
        get_values_button = wx.Button(panel, label="Get Column 1 Values")
        get_values_button.Bind(wx.EVT_BUTTON, self.on_get_values)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(get_values_button, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(sizer)

    def on_get_values(self, event):
        # Obtener los valores de la columna 1
        column1_values = []
        item_count = self.list_ctrl.GetItemCount()

        for index in range(item_count):
            column1_values.append(self.list_ctrl.GetItemText(index, 0))

        # Mostrar los valores en una ventana de mensaje
        wx.MessageBox("Column 1 Values:\n" + "\n".join(column1_values), "Info", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
