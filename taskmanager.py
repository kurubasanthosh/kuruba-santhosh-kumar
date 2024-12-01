import tkinter as tk
from tkinter import messagebox, ttk

class taskmanagerapp:
    def __init__(self,root):
        self.root = root
        self.root.title("task manager")
        self.task=[]
        self.create_task_form()
        self.create_task_list()
        self.create_filter_dropdown()

    def create_task_form(self):
        form_frame=tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame,text="title:").grid(row=0,column=0,padx=5,pady=5)
        self.title_entry=tk.Entry(form_frame,width=30)
        self.title_entry.grid(row=0,column=1,padx=5,pady=5)

        tk.Label(form_frame,text="description:").grid(row=1,column=0,padx=5,pady=5)
        self.discription_entry=tk.Entry(form_frame,width=30)
        self.discription_entry.grid(row=1,column=1,padx=5,pady=5)

        tk.Label(form_frame,text="status:").grid(row=2,column=0,padx=5,pady=5)
        self.status_var=tk.StringVar(value="to do")
        self.status_menu=ttk.Combobox(form_frame,textvariable=self.status_var,value=["to do","in progress","done"],state="readonly")
        self.status_menu.grid(row=2,column=1,padx=5,pady=5)

        add_button=tk.Button(form_frame,text="add task",command=self.add_task)
        add_button.grid(row=3,column=0,columnspan=2,pady=10)

    def create_task_list(self):
        self.task_list_frame=tk.Frame(self.root)
        self.task_list_frame.pack(pady=10)

        self. task_tree = ttk. Treeview(self. task_list_frame, columns=("Title", "Description", "Status"), show="headings")
        self. task_tree.heading("Title", text="Title")
        self. task_tree.heading ("Description", text="Description") 
        self. task_tree.heading ("Status", text="Status") 
        self.task_tree.pack(side=tk.LEFT, padx=5)
        
        scrollbar = ttk.Scrollbar(self.task_list_frame, orient=tk.VERTICAL, command=self. task_tree.yview)
        self.task_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        button_frame=tk.Frame(self.root)
        button_frame.pack(pady=10)

        update_button=tk.Button(button_frame,text="update status",command=self.update_task_status)
        update_button.grid(row=0,column=0,padx=5)

        delete_button=tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=0, column=1, padx=5)
    def create_filter_dropdown (self):
        filter_frame = tk. Frame(self.root)
        filter_frame. pack(pady=10)
        
        tk. Label(filter_frame, text="Filter by Status:"). pack(side=tk. LEFT, padx=5)
        self. filter_var = tk.StringVar(value="All" )
        filter_menu = ttk.Combobox(filter_frame, textvariable=self.filter_var, values=["All", "To Do", "In Progress", "Done"],state=" readonly")
        filter_menu.pack(side=tk.LEFT, padx=5)
        filter_menu.bind ("«ComboboxSelected>>", self.filter_tasks)
    
    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.description_entryget().strip()
        status = self.status_var.get()
        
        if not title:
            messagebox.showerror("Error", "Title is required!")
            return
        
        total_tasks = len (self. tasks)
        todo_count = len([task for task in self.tasks if task[2] == "To Do"])
        if status == "to do" and todo_count>=total_tasks/2:
            messagebox. showerror("Error""Cannot create more 'To Do' tasks. Current 'To Do' tasks ({todo_count}) " f"are >= 50% of total tasks ({total_tasks}).")
            return
        
        self.tasks.append ((title, description, status))
        self. refresh_task_list()
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk. END)
    
    def update_task_status(self):
        selected_item = self.task_tree.selection ()
        if not selected_item:
            messagebox. showerror("Error", "No task selected!")
            return
        
        task_index = self.task_tree.index(selected_item[0])
        current_status = self.tasks [task_index] [2]
        next_status = {"To Do": "In Progress","In Progress": "Done","Done": "Done"}
        updated_task = self.tasks[task_index][:2] + (next_status[current_status],)
        self.tasks [task_index] = updated_task
        self. refresh_task_list()
    
    def delete_task(self):
        selected_item= self. task_tree. selection()
        if not selected_item:
            messagebox. showerror("Error", "No task selected!")
            return
        
        task_index= self. task_tree. index(selected_item[0])
        del self. tasks[task_index]
        self. refresh_task_list()

    def filter_tasks(self, event=None):
        filter_value = self.filter_var.get()
        self. refresh_task_list(filter_value)
    
    def refresh_task_list(self, filter_value="All"):
        for item in self. task_tree.get_children():
            self. task_tree.delete (item)

        for task in self.tasks:
            if filter_value=="all"or task[2]==filter_value:
                self.task_tree.insert("",tk.END,values=task)
if __name__=="__main__":
    root=tk.Tk()
    app=taskmanagerapp(root)
    root.mainloop()








