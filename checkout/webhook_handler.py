from django.http import HttpResponse


class StripeWH_Handler:
    # Stripe Webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # Handle Generic/Unknown/Unexpected webhook events

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}', status=200)

    def handle_event_intent_succeeded(self, event):
        # Handle payment intent succeeded webhook events

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)

    def handle_event_intent_payment_failed(self, event):
        # Handle payment intent failure webhook events

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
