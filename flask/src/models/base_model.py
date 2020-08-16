class BaseModel(object):
    def __repr__(self):
        values = vars(self).values()
        shortened_values_str = [str(v)[:10] for v in values]

        return f"{self.__class__.__name__}({', '.join(shortened_values_str)})"