class SingleTonMeta(type): 
    _instance = dict()
    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instance: 
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]