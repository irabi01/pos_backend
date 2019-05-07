from django.contrib import admin
from .models import (
TbUsers,
TbGroup,
TbGroupUsers,
TbRoles,
TbAccessRights,
TbPOS,
TbAssignPOS,
TbTenderType,
TbTax,
TbTerms,
TbInventoryCategories,
TbAccounts,
TbInventoryAccounts,
TbStores,
TbItemDefinition,
TbInventoryControls,
TbInventoryTransactions,
TbSupplierCategories,
TbSuppliers)

# Register your models here.
admin.site.register(TbUsers)
admin.site.register(TbGroup)
admin.site.register(TbGroupUsers)
admin.site.register(TbRoles)
admin.site.register(TbAccessRights)
admin.site.register(TbPOS)
admin.site.register(TbAssignPOS)
admin.site.register(TbTenderType)
admin.site.register(TbTax)
admin.site.register(TbTerms)
admin.site.register(TbInventoryCategories)
admin.site.register(TbAccounts)
admin.site.register(TbInventoryAccounts)
admin.site.register(TbStores)
admin.site.register(TbItemDefinition)
admin.site.register(TbInventoryControls)
admin.site.register(TbInventoryTransactions)
admin.site.register(TbSupplierCategories)
admin.site.register(TbSuppliers)
