from application.model.entity.category_entity import Category
from application.model.dao.movie_dao import Movie_DAO


class Category_DAO:
    def __init__(self):

        self._categorias = []
        self._categorias.append(Category(1, "Comida", "é só comida",))
        self._categorias.append(Category(2, "Comida ruim", "é só comida",))
        self._categorias.append(Category(3, "Comida mais ou menos", "é só comida",))

    def getListCategory(self):
        return self._categorias

    def getCategoryById(self, id):
        for i, category in enumerate(self.getListCategory()):
            if category.getId() == id:
                return category
        return None
