class EnvManager():
    def __init__(self):
        self.vars = {}
        self.count = 0
        self.fun_scope = {}
        self.fun_scope_counter = 0
        self.fun = set()
        self.label = 0
        self.jz_labels = []

    def add_var(self, name):
        self.vars[name] = self.count
        self.count += 1

    def get_var(self, name):
        if name not in self.fun_scope:
            return self.vars[name]
        else:
            return self.fun_scope[name]

    def var_exists(self, name):
        return name in self.vars or name in self.fun_scope

    def fun_exists(self, name):
        return name in self.fun

    def add_fun(self, name):
        self.fun.add(name)

    def add_fun_var(self, name):
        self.fun_scope[name] = self.count+self.fun_scope_counter
        self.fun_scope_counter += 1
        
    def pop_fun_scope(self):
        self.fun_scope.clear()
        self.fun_scope_counter = 0

    def new_label(self):
        self.label += 1

    def get_label(self):
        return self.label

    def push_jz_label(self):
        self.jz_labels.append(self.label)
    
    def pop_jz_label(self):
        return self.jz_labels.pop()


    
