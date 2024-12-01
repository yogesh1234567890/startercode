# from flask import Blueprint, request, jsonify, g
# from sqlalchemy.exc import IntegrityError
# from app.models import Event, Booking, Ticket
# from app.database import db
# from utils.stripe_config import create_stripe_payment_intent
# from utils.redis_config import lock_tickets, unlock_tickets

# ticket_routes = Blueprint('api', __name__)

# @ticket_routes.route('/events/<int:event_id>/book', methods=['POST'])
# def book_tickets(event_id):
#     try:
#         data = request.get_json()
#         user_id = data.get('user_id')
#         quantity = data.get('quantity')

#         if not user_id or not quantity or quantity <= 0:
#             return jsonify({"error": "Invalid input"}), 400

#         event = Event.query.get(event_id)
#         if not event:
#             return jsonify({"error": "Event not found"}), 404

#         locked = lock_tickets(event_id, quantity, user_id)
#         if not locked:
#             return jsonify({"error": "Tickets not available"}), 409

#         # Create Stripe Payment Intent
#         payment_intent = create_stripe_payment_intent(
#             amount=event.price * quantity,
#             currency='usd',
#             metadata={"event_id": event_id, "user_id": user_id}
#         )

#         # Create a booking in the database
#         booking = Booking(
#             user_id=user_id,
#             event_id=event_id,
#             quantity=quantity,
#             stripe_payment_id=payment_intent['id'],
#             status='Pending'
#         )
#         db.session.add(booking)
#         db.session.commit()

#         # Return the payment intent client secret
#         return jsonify({
#             "message": "Tickets locked. Complete payment to confirm booking.",
#             "payment_client_secret": payment_intent['client_secret'],
#             "booking_id": booking.id
#         }), 200

#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({"error": "Could not process booking"}), 500
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
