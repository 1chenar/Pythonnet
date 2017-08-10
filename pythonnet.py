import clr

clr.AddReference(r"wpf\PresentationFramework")
from System.IO import StreamReader
from System.Windows.Markup import XamlReader
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Windows import Application, Window
from System.Windows import MessageBox

class MyWindow(Window):
    def __init__(self):
        stream = StreamReader("pythonnet.xaml")
        window = XamlReader.Load(stream.BaseStream)
        Application().Run(window)

    def Button_Click(self):
        MessageBox.Show("Hi!")

if __name__ == '__main__':
    thread = Thread(ThreadStart(MyWindow))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()