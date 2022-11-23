from django.shortcuts import render, redirect, HttpResponse
from .models import addProduct, saleProduct, add_Purchase, add_Member
import xlsxwriter
# Create your views here.

def index(request):
    return render(request, "index.html")

def yourDashboard(request):
    if request.method == "POST":
        return render(request, "yourDashboard.html")
    else:
        return render(request, "yourDashboard.html")

def addSaleProduct(request):
    itemSuccessfulllyAdded=False
    wrongInput = False
    if request.method == "POST":
        try:
            productName = request.POST['productName']
            unit = request.POST['unit']
            stock = request.POST['stock']
            particulars = request.POST['particulars']
            rate = request.POST['rate']
            curBal = float(rate)*float(stock)



            #print("Product Name:", productName, "Unit:", unit, "Stock:", stock, "Rate:", rate, "Particulars:", particulars, "CurBal:",curBal)
            if particulars.strip(" ") == "" or productName.strip(" ") == "" or len(stock.strip(" ")) <= 0 or len(rate.strip(" ")) <= 0:
                print("Please Provide valid !")
                wrongInput = True
                return render(request, "addSaleProduct.html", {'wrongInput': wrongInput})
            else:
                #print("Product Name:", productName, "Unit:", unit, "Stock:", stock)
                items = addProduct(productName=productName, unit=unit, stock=stock, rate=rate, particulars=particulars, curBal=curBal)
                items.save()

                itemSuccessfulllyAdded=True
                return render(request, "addSaleProduct.html", {'itemSuccessfulllyAdded': itemSuccessfulllyAdded})
        except:
            print("In Exception")
            wrongInput = True
            return render(request, "addSaleProduct.html", {'wrongInput': wrongInput})
    else:
        return render(request, "addSaleProduct.html")


def viewProduct(request):
    if request.method == "POST":
        items = addProduct.objects.all()
        return render(request, "viewProduct.html", {'items': items})
    else:
        items = addProduct.objects.all()
        return render(request, "viewProduct.html", {'items': items})

def delete(request, id):
    obj = addProduct.objects.get(id=id)
    obj.delete()
    return redirect('viewProduct')

def deleteUpdate(request, id):
    obj = addProduct.objects.get(id=id)
    obj.delete()
    return redirect('updateStock')

def edit(request, id):
    obj = addProduct.objects.get(id=id)
    if request.method == "POST":
        try:
            productName = request.POST['productName']
            unit = request.POST['unit']
            stock = request.POST['stock']
            rate = request.POST['rate']
            particulars = request.POST['particulars']
            #print("Product Name:", productName, "Unit:", unit, "Stock:", stock, "Rate: ", rate, "Particulars:", particulars)
            if particulars.strip(" ") == "" or productName.strip(" ") == "" or len(stock.strip(" ")) <= 0 or len(rate.strip(" ")) <= 0:
                print("Please Provide valid !")
                wrongInput = True
                return render(request, "editProduct.html", {'wrongInput': wrongInput})
            else:
                # print("Product Name:", productName, "Unit:", unit, "Stock:", stock)
                obj.productName = productName
                obj.unit = unit
                obj.stock = stock
                obj.rate = rate
                obj.particulars = particulars
                obj.curBal = float(rate)*float(stock)
                obj.save()

                itemSuccessfulllyAdded = True
                return redirect("viewProduct")
        except:
            return HttpResponse("<center><h1>Sorry an exception occurred !!!</h1></center>")

    else:
        product = obj.productName
        unit = obj.unit
        stock = obj.stock
        rate = obj.rate
        particulars = obj.particulars
        print(product, stock, unit)

        return render(request, "editProduct.html", {'productName': product, 'unit': unit,
                                                    'stock': stock, 'rate': rate, 'particulars': particulars})
    #return redirect('viewProduct')

def excel(request):
    items = addProduct.objects.all()
    row=1
    #Write into excel
    with xlsxwriter.Workbook("chcknow.xlsx") as workbook:
        workshit = workbook.add_worksheet()
        workshit.write("A1", "Date")
        workshit.write("B1", "Product Name")
        workshit.write("C1", "Stock")
        workshit.write("D1", "Particulars")
        workshit.write("E1", "Rate")
        workshit.write("F1", "Opening Balance")
        workshit.write("G1", "Closing Balance")
        workshit.write("H1", "Current Balance")
        for item in items:
            row = row + 1
            workshit.write("A" + str(row), str(item.date))
            workshit.write("B" + str(row), item.productName)
            workshit.write("C" + str(row), item.stock)
            workshit.write("D" + str(row), item.particulars)
            workshit.write("E" + str(row), item.rate)
            workshit.write("F" + str(row), item.openBal)
            workshit.write("G" + str(row), item.clsBal)
            workshit.write("H" + str(row), item.curBal)
    return redirect('updateStock')

def updateStock(request):
    total=0
    obj = addProduct.objects.all()
    for i in obj:
        total+=i.curBal
    print(total)
    return render(request, "updateStock.html", {'items': obj, 'total': total})

def selectSale(request):
    obj = addProduct.objects.all()
    return render(request, "saleProducts.html", {'items': obj})

def saleThis(request, id):
    opt = False
    if request.method == "POST":
        try:
            qty = request.POST['qty']
            customerName = request.POST['customerName']
            invoiceNumber = request.POST['invoiceNumber']

            customerGstin = request.POST['customerGstin']
            taxableValue = request.POST['taxableValue']
            cgst = request.POST['cgst']
            sgst = request.POST['sgst']
            igst = request.POST['igst']
            totalGst = request.POST['totalGst']
            totalGst = float(totalGst)
            totalGst = float(round(totalGst, 2))
            total = request.POST['total']
            total = float(total)
            total = float(round(total, 2))
            discount = request.POST['discount']
            discount=float(discount)
            discount = float(round(discount, 2))
            due = request.POST['due']
            due = float(due)
            due = float(round(due, 2))
            paymentMethod = request.POST['paymentMethod']
            invoiceValue = request.POST['invoiceValue']


            if float(qty) > 0:

                #Product update is here
                obj = addProduct.objects.get(id=id)
                stock = obj.stock
                rate = obj.rate
                obj.stock = float(stock) - float(qty)
                obj.save()
                obj = addProduct.objects.get(id=id)
                rt = obj.rate
                st = obj.stock
                obj.curBal = float(rt)*float(st)
                obj.save()

                #Generate Selling Report
                obj1 = addProduct.objects.get(id=id)
                productName = obj1.productName
                obj1.save()


                obj2 = saleProduct(customerName=customerName,
                                   productName=productName, qty=float(qty),
                                   invoiceNumber=float(invoiceNumber),
                                   customerGstin=float(customerGstin), taxableValue=float(taxableValue),
                                   cgst=float(cgst), sgst=float(sgst), igst=float(igst),
                                   totalGst=float(totalGst), total=float(total),
                                   discount=float(discount), due=float(due),
                                   paymentMethod=paymentMethod,
                                   invoiceValue=float(invoiceValue))

                obj2.save()


                return render(request, "sale.html", {'opt': True})
            else:
                return HttpResponse("<center><h2 style='color: red;'> Sorry Something went wrong!!! Please fill the all field properly !!!</h2></center>")
        except:
            print("in except")
            return HttpResponse("<center><h2 style='color: red;'> Sorry Something went wrong!!! Please fill the all field properly !!!</h2></center>")
    else:
        #Product in GET request
        obj = addProduct.objects.get(id=id)
        thisId = id
        product = obj.productName
        unit = obj.unit
        stock = obj.stock
        rate = obj.rate
        particulars = obj.particulars

        return render(request, "sale.html", {'product': product, 'unit': unit, 'stock': stock, 'rate': rate, 'particulars': particulars, 'id': thisId})

def viewPurchase(request):
    if request.method == "POST":
        cat = request.POST['category']

        obj = add_Purchase.objects.filter(category=cat)
        return render(request, "viewPurchase.html", {"items": obj})
    else:
        return render(request, "viewPurchase.html")


def shareCertificate(request):
    return render(request, "shareCertificate.html")

def addShareCertificate(request):
    return render(request, "addShareRegister.html")


def viewSaleReport(request):
    if request.method == "POST":
        try:
            product = request.POST['productName']
            allitems = saleProduct.objects.all()
            obj = saleProduct.objects.filter(productName=product)
            items = addProduct.objects.filter(productName=product)

            stock=""
            products=""
            for i in items:
                stock=i.stock
                products=i.productName

            return render(request, "viewSaleReport.html", {'info': obj, 'stock': stock, 'all': allitems,
                                                           'products': products, 'post': True})
        except:
            print("In except")
            obj = saleProduct.objects.all()
            return render(request, "viewSaleReport.html", {'obj': obj})
    else:
        obj = saleProduct.objects.all()
        return render(request, "viewSaleReport.html", {'all': obj})


def addMember(request):
    if request.method == "POST":
        try:
            memberId = request.POST['memberId']
            memberPhoto = request.FILES['myPhoto']
            memberName = request.POST['memberName']
            gurdianName = request.POST['gurdianName']
            phoneNo = request.POST['phoneNo']
            gender = request.POST['gender']
            category = request.POST['category']
            landHolding = request.POST['landHolding']
            memberType = request.POST['memberType']
            familyMember = request.POST['familyMember']
            block = request.POST['block']
            village = request.POST['village']
            district = request.POST['district']
            state = request.POST['state']
            cropName = request.POST['cropName']
            irrigationSource = request.POST['irrigationSource']
            bankName = request.POST['bankName']
            ifsc = request.POST['ifsc']
            kccLimit = request.POST['kccLimit']
            aadharNumber = request.POST['aadharNumber']

            obj = add_Member(memberId=int(memberId), memberPhoto=memberPhoto, memberName=memberName, memberType=memberType,
                             gurdianName=gurdianName,
                             phoneNo=int(phoneNo), gender=gender, category=category, landHolding=landHolding,
                             district=district,
                             familyMember=familyMember, block=block, village=village, state=state,
                             cropName=cropName,
                             irrigationSource=irrigationSource, kccLimit=kccLimit, bankName=bankName,
                             ifscCode=ifsc,
                             aadharNo=aadharNumber
                             )
            obj.save()

            return HttpResponse("Done !!!")

        except:
            print("In add member except area ...")
            return HttpResponse("An exception occured !!!")
    else:
        return render(request, "addMember.html")


def viewMember(request):
    obj = add_Member.objects.all()
    return render(request, "viewMember.html", {'items': obj})

def addPurchase(request):
    if request.method == "POST":
        try:
            category = request.POST['category']
            qty = request.POST['qty']
            productName = request.POST['productName']
            invoiceNumber = request.POST['invoiceNumber']
            unit = request.POST['unit']
            supplierName = request.POST['supplierName']

            taxableValue = request.POST['taxableValue']
            cgst = request.POST['cgst']
            sgst = request.POST['sgst']
            igst = request.POST['igst']
            totalGst = request.POST['totalGst']
            totalGst = float(totalGst)
            totalGst = float(round(totalGst, 2))

            total = request.POST['total']
            total = float(total)
            total = float(round(total, 2))

            invoiceValue = request.POST['invoiceValue']
            invoiceValue = int(invoiceValue)


            paymentMethod = request.POST['paymentMethod']
            paymentId = request.POST['paymentId']
            if int(qty) > 0:
                obj = add_Purchase(category=category, supplierName=supplierName,productName=productName,
                                   qty=qty, invoiceNumber=invoiceNumber, unit=unit, taxableValue=taxableValue,
                                   cgst=cgst, sgst=sgst, igst=igst, totalGst=totalGst, total=total,
                                   paymentMethod=paymentMethod, paymentId=paymentId, invoiceValue=invoiceValue)
                obj.save()

                return redirect("yourDashboard")
            else:
                return render(request, "addPurchase.html")
        except:
            print("In add purcahse except area ...")
            return HttpResponse("An exception occured !!!")
    else:
        return render(request, "addPurchase.html")