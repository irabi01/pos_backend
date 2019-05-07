from __future__ import unicode_literals
from django.db import models

# Create your models here.
class TbUsers(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    GENDERS = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender = models.CharField(max_length = 10, choices=GENDERS, default='Male')
    DateOfBirth = models.DateField()
    Email = models.EmailField(default = '')
    Mobile = models.PositiveIntegerField(default = 755228899)
    Status = models.BooleanField(default = 'false')
    class Meta:
        verbose_name_plural = "POS-User"
    def __str__(self):
        return self.Email

class TbGroup(models.Model):
    Group_name = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Groups"
    def __str__(self):
        return self.Group_name


class TbGroupUsers(models.Model):
    Group_id = models.ForeignKey(TbGroup, on_delete = models.CASCADE)
    User_id = models.ForeignKey(TbUsers, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = "Users-Groups"
    # def __str__(self):
    #     return self.id

class TbRoles(models.Model):
    Role = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Roles"
    def __str__(self):
        return self.Role

class TbAccessRights(models.Model):
    Group_id = models.ForeignKey(TbGroup, on_delete = models.CASCADE)
    Role_id = models.ForeignKey(TbRoles, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = "Access Rights"
    # def __str__(self):
    #     return self.Group_id

class TbPOS(models.Model):
    Pos_name = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Point of sale"
    def __str__(self):
        return self.Pos_name

class TbAssignPOS(models.Model):
    Pos_id = models.ForeignKey(TbPOS, on_delete = models.CASCADE)
    User_id = models.ForeignKey(TbUsers, on_delete = models.CASCADE)
    POS_STATUS = (
        ('In-Use','In-Use'),
        ('Occupied','Occupied'),
        ('Open','Open'),
    )
    Status = models.CharField(max_length = 50, choices=POS_STATUS, default='Open')
    class Meta:
        verbose_name_plural = "Assign POS"
    # def __str__(self):
    #     return self.Pos_id

class TbTenderType(models.Model):
    Tender_type = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Tender Type"
    def __str__(self):
        return self.Tender_type


class TbTax(models.Model):
    Tax_code = models.CharField(max_length = 50)
    Tax_name = models.CharField(max_length = 50)
    Rate = models.FloatField()
    class Meta:
        verbose_name_plural = "Tax"
    def __str__(self):
        return self.Tax_code

class TbTerms(models.Model):
    Term_name = models.CharField(max_length = 50)
    Term_code = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Terms"
    def __str__(self):
        return self.Term_name


class TbInventoryCategories(models.Model):
    Category_code = models.CharField(max_length = 50)
    Category_name = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Inventory Categories"
    def __str__(self):
        return self.Category_name


class TbAccounts(models.Model):
    Account_code = models.CharField(max_length = 50)
    Account_name = models.CharField(max_length = 50)
    Account_type = models.PositiveIntegerField()
    class Meta:
        verbose_name_plural = "Accounts"
    def __str__(self):
        return self.Account_name


class TbInventoryAccounts(models.Model):
    Category_id = models.ForeignKey(TbInventoryCategories, on_delete = models.CASCADE)
    Account_id = models.ForeignKey(TbAccounts, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = "Inventory Accounts"
    # def __str__(self):
    #     return self.Category_id


class TbStores(models.Model):
    Store_code = models.CharField(max_length = 50)
    Store_name = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Stores"
    def __str__(self):
        return self.Store_name


class TbItemDefinition(models.Model):
    Barcode1 = models.CharField(max_length = 50)
    Barcode2 = models.CharField(max_length = 50)
    Description = models.CharField(max_length = 50)
    BuyQty = models.FloatField()
    BuyUnit = models.FloatField()
    StockQty = models.FloatField()
    StockUnit = models.FloatField()
    Category_id = models.ForeignKey(TbInventoryCategories, on_delete = models.CASCADE)
    OpenQtyTotalValue = models.FloatField()
    OpenQtyAvgValue = models.FloatField()
    OpenQty = models.FloatField()
    AlocatedQty = models.FloatField()
    OrderQty = models.FloatField()
    ReorderLevelQty = models.FloatField()
    UnitSellingPrice = models.FloatField()
    Tax_id = models.ForeignKey(TbTax, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = "Items Definition"
    def __str__(self):
        return self.Barcode1


class TbInventoryControls(models.Model):
    Store_id = models.ForeignKey(TbStores, on_delete = models.CASCADE)
    OpenQtyTotalValue = models.FloatField()
    OpenQtyAvgValue = models.FloatField()
    OpenQty = models.FloatField()
    AlocatedQty = models.FloatField()
    OrderQty = models.FloatField()
    ReorderLevelQty = models.FloatField()
    class Meta:
        verbose_name_plural = "Inventory Control"
    def __str__(self):
        return self.OpenQtyTotalValue


class TbInventoryTransactions(models.Model):
    Item_id = models.ForeignKey(TbItemDefinition, on_delete = models.CASCADE)
    Store_id = models.ForeignKey(TbStores, on_delete = models.CASCADE)
    Transaction_number = models.CharField(max_length = 50)
    Quantity = models.FloatField()
    Date = models.DateField()
    class Meta:
        verbose_name_plural = "Inventory Transaction"
    def __str__(self):
        return self.Transaction_number


class TbSupplierCategories(models.Model):
    Category_name = models.CharField(max_length = 50)
    Category_code = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = "Supplier Categories"
    def __str__(self):
        return self.Category_name


class TbSuppliers(models.Model):
    Supplier_name = models.CharField(max_length = 50)
    Supplier_category_id = models.ForeignKey(TbSupplierCategories, on_delete = models.CASCADE)
    Telephone_number = models.CharField(max_length = 15)
    Email = models.EmailField()
    Street = models.CharField(max_length = 50)
    Representative_name = models.CharField(max_length = 50)
    Representative_mobile = models.CharField(max_length = 15)
    class Meta:
        verbose_name_plural = "Suppliers"
    def __str__(self):
        return self.Supplier_name
