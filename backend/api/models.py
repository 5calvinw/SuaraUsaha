from django.db import models

class users(models.Model):
    # id = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    business_name = models.CharField(max_length=100)
    business_desc = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class inventory(models.Model):
    # id = models.IntegerField()
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=120)
    is_sellable = models.BooleanField()
    sell_price = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=12, decimal_places=3)
    unit = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} - ({self.qty} {self.unit})"


class finances(models.Model):
    # id = models.IntegerField()
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    starting_cash = models.DecimalField(max_digits=15, decimal_places=2)
    monthly_expense = models.DecimalField(max_digits=15, decimal_places=2)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Monthly Expense : {self.monthly_expense}, Current Balance : {self.current_balance}"

class finances_log(models.Model):
    # id = models.IntegerField()
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    date = models.DateTimeField()

    TYPE_CHOICES = [
        ('sale', 'Sale'),
        ('expense', 'Expense'),
        ('loss', 'Loss'),
        ('income', 'Income'),
        ('other', 'Other'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    desc = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('qris', 'Qris'),
        ('transfer', 'Transfer'),
        ('ewallet', 'Ewallet'),
        ('other', 'Other'),
    ]

    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} via {self.payment_type} of {self.amount} for {self.desc}"
    
class inventory_log(models.Model):
    # id = models.IntegerField()
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(inventory, on_delete=models.CASCADE)
    date = models.DateTimeField()

    ACTION_CHOICES = [
        ('add', 'Add'),
        ('remove', 'Remove')
    ]

    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    desc = models.CharField(max_length=255)
    qty = models.DecimalField(max_digits=12, decimal_places=3)
    unit = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.action} | {self.desc} - ({self.qty} {self.unit})"
    

class documents(models.Model):
    # id = models.IntegerField()
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    file = models.BinaryField()
    desc = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"test document message"




    
