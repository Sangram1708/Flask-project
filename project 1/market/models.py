from market import db
class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),unique=True,nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=12),unique=True,nullable=False)
    description=db.Column(db.String(length=1040),unique=True,nullable=False)

    def __repr__(self):
        return f"username:{self.name },price{self.price },barcode:{self.barcode }"