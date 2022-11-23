from django.db import models
import datetime as d
# Create your models here.
class addProduct(models.Model):
    date = models.DateTimeField(auto_created=True, default=d.datetime.today())
    productName = models.CharField(max_length=200, default="N/A")
    unit = models.CharField(max_length=10, default="N/A")
    stock = models.FloatField(default=0)
    rate = models.FloatField(default=0)
    particulars = models.CharField(max_length=350, default="N/A")
    openBal = models.FloatField(default=0)
    clsBal = models.FloatField(default=0)
    curBal = models.FloatField(default=0)
    def __str__(self):
        return self.productName

class saleProduct(models.Model):
    productName = models.CharField(max_length=200, default="N/A")
    invoiceNumber = models.FloatField(default=0)
    invoiceDate = models.DateTimeField(auto_created=True, default=d.datetime.today())
    customerName = models.CharField(max_length=200, default="N/A")
    customerGstin = models.FloatField(max_length=30, default=0)
    qty = models.FloatField(max_length=30, default=0)
    taxableValue = models.FloatField(max_length=30, default=0)
    cgst = models.FloatField(max_length=30, default=0)
    sgst = models.FloatField(max_length=30, default=0)
    igst = models.FloatField(max_length=30, default=0)
    totalGst = models.FloatField(max_length=30, default=0)
    total = models.FloatField(max_length=30, default=0)
    discount = models.FloatField(max_length=30, default=0)
    due = models.FloatField(max_length=30, default=0)
    paymentMethod = models.CharField(max_length=350, default="N/A")
    invoiceValue = models.FloatField(max_length=30, default=0)

    def __str__(self):
        return self.customerName+" :- "+self.productName

class add_Purchase(models.Model):
    category = models.CharField(max_length=80, default="N/A")
    productName = models.CharField(max_length=200, default="N/A")
    invoiceNumber = models.IntegerField(default=0)
    invoiceDate = models.DateTimeField(auto_created=True, default=d.datetime.today())

    unit = models.CharField(max_length=50, default="N/A")
    qty = models.IntegerField(default=0)
    supplierName = models.CharField(max_length=150, default="N/A")
    taxableValue = models.FloatField(default=0)
    cgst = models.FloatField(default=0)
    sgst = models.FloatField(default=0)
    igst = models.FloatField(default=0)
    totalGst = models.FloatField(default=0)
    total = models.FloatField(default=0)
    invoiceValue = models.IntegerField(default=0)
    paymentMethod = models.CharField(max_length=350, default="N/A")
    paymentId = models.IntegerField(default=0)

    def __str__(self):
        return self.supplierName+" :- "+self.productName

class add_Member(models.Model):
    memberId = models.IntegerField(default=0)
    memberPhoto = models.ImageField(upload_to="MemberPhoto/", default=None, blank=True, null=True)
    memberName = models.CharField(max_length=250, default="N/A")
    gurdianName = models.CharField(max_length=250, default="N/A")
    phoneNo = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, default="N/A")
    category = models.CharField(max_length=60, default="N/A")
    landHolding = models.CharField(max_length=50, default="N/A")
    memberType = models.CharField(max_length=50, default="N/A")
    familyMember = models.CharField(max_length=90, default="N/A")
    block = models.CharField(max_length=150, default="N/A")
    village = models.CharField(max_length=250, default="N/A")
    district = models.CharField(max_length=150, default="N/A")
    state = models.CharField(max_length=150, default="N/A")
    cropName = models.CharField(max_length=150, default="N/A")
    irrigationSource = models.CharField(max_length=150, default="N/A")
    kccLimit = models.CharField(max_length=150, default="N/A")
    bankName = models.CharField(max_length=250, default="N/A")
    ifscCode = models.CharField(max_length=250, default="N/A")
    aadharNo = models.CharField(max_length=12, default="N/A")

    def __str__(self):
        return self.memberName+" :- "+str(self.memberId)
