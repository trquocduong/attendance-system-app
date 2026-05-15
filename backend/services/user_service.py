from models.user_model import User
from auth import hash_pwd, verify_password


def get_user_service(db):
    users = db.query(User).all()
    return users


def create_user_service(db, user):
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_pwd(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def put_user_service(db, user, user_id):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        db.close()
        return {
            "message": "User not found"
        }
    existing_user.name = user.name
    existing_user.email = user.email
    db.commit()
    db.refresh(existing_user)
    return existing_user


def del_user_service(db, user_id):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        db.close()
        return {
            "message": "User not found"
        }
    db.delete(existing_user)
    db.commit()
    return existing_user


def login_auth_service(db, user):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        db.close()

        return {
            "message": "Email not found"
        }

    is_valid = verify_password(
        user.password,
        existing_user.password
    )

    if not is_valid:
        db.close()

        return {
            "message": "Invalid password"
        }
    return existing_user
