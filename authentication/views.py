from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView


# OOP Sign In
class SignInView(TokenObtainPairView):
    """
    View untuk login. Mewarisi TokenObtainPairView dari SimpleJWT.
    Menerima POST dengan 'username' dan 'password'.
    Mengembalikan 'access' dan 'refresh' token.
    """

    pass


# OOP Sign Out
class SignOutView(TokenBlacklistView):
    """
    View untuk logout. Mewarisi TokenBlacklistView dari SimpleJWT.
    Menerima POST dengan 'refresh' token.
    Token tersebut akan dimasukkan ke database blacklist dan tidak bisa dipakai lagi.
    """

    pass
