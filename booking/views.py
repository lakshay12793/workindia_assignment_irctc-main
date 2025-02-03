from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db import transaction
from .models import CustomUser, Train, Booking
from .serializers import UserSerializer, TrainSerializer, BookingSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = CustomUser.objects.create_user(
            username=serializer.data['username'],
            password=serializer.data['password'],
            is_admin=serializer.data['is_admin']
        )
        return Response({'message': 'User registered successfully!'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_train(request):
    if not request.user.is_admin:
        return Response({'error': 'Not authorized'}, status=403)
    
    data = request.data
    train = Train.objects.create(
        source=data['source'],
        destination=data['destination'],
        total_seats=data['total_seats'],
        available_seats=data['total_seats']
    )
    return Response({'message': 'Train added successfully!'})


@api_view(['GET'])
def check_availability(request, source, destination):
    trains = Train.objects.filter(source=source, destination=destination)
    serializer = TrainSerializer(trains, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
@transaction.atomic
def book_seat(request):
    try:
        train_id = request.data.get('train_id')
        train = Train.objects.select_for_update().get(id=train_id)
        if train.available_seats > 0:
            train.available_seats -= 1
            train.save()
            booking = Booking.objects.create(
                user=request.user,
                train=train,
                seats_booked=1
            )
            return Response({'message': 'Seat booked successfully!'})
        else:
            return Response({'error': 'No seats available'}, status=400)
    except Train.DoesNotExist:
        return Response({'error': 'Train not found'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_booking_details(request):
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
