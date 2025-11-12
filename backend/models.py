from django.db import models


class User(models.Model):
    SEX_CHOICES = [(0, 'Male'), (1, 'Female'), (2, 'Other')]
    ROLE_CHOICES = [(0, 'Admin'), (1, 'Vendor'),
                    (2, 'Customer'), (3, 'Delivery')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=128)  # for hashed password
    sex = models.IntegerField(choices=SEX_CHOICES)
    date_of_birth = models.DateField()
    role = models.IntegerField(choices=ROLE_CHOICES)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.TextField(null=True, blank=True)
    product_price = models.FloatField(default=0)
    product_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    product_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name or "Unnamed Product"


class Image(models.Model):
    # ✅ Use a clear related_name to avoid clashes
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",  # one product can have multiple images
    )
    image_name = models.TextField()

    def __str__(self):
        return self.image_name


class Order(models.Model):
    order_name = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.product}"
