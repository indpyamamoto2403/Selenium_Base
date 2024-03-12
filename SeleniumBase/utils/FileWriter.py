import openpyxl
class FileWriter:
    '''
    FileをロードするためのClass
    '''
    def __init__(self,filepath):
        self.filepath = filepath
    
    def load(self):
        pass
    
    def show_filepath(self):
        print(f"{self.filepath}を読み込みました。")




class ExcelWriter(FileWriter):
    '''
    ExcelをLoadするための
    '''
    def __init__(self,filepath):
        super().__init__(filepath)
        self.wb = openpyxl.load_workbook(filename=filepath, read_only=False)
        self.ws = self.wb.active
        
    def load(self):
        pass
    
    def write(self,row,col, value)->str:
        cell = self.ws.cell(row=row, column=col)
        cell.value = value
        self.wb.save(self.filepath)  
    
                  