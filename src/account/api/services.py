from django.contrib.auth import get_user_model

def create_user(*, email: str, password: str, first_name: str, last_name: str):
    """
    Create a new user.
    """
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    return user

def update_user(instance, **kwargs):
    """
    Update an existing user.
    """
    for attr, value in kwargs.items():
        setattr(instance, attr, value)
    instance.save()

    return instance

def delete_user(instance) -> None:
    """
    Delete a user.
    """
    instance.delete()

def change_password(instance, old_password: str, new_password: str):
    """
    Change the password of a user.
    """
    if not instance.check_password(old_password):
        raise ValueError("Old password is incorrect.")
    
    instance.set_password(new_password)
    instance.save()