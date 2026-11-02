package com.journey.exercises.designpatterns;

/**
 * Exercise EX-07-1: God Class Anti-Pattern
 * 
 * This class violates all 5 SOLID principles:
 * - SRP: Handles validation, pricing, payment, database persistence, and emailing.
 * - OCP: Switch/if statements require editing this file every time a payment method or tax rate is added.
 * - LSP: Subclasses would break preconditions or expectations.
 * - ISP: Forces clients to depend on everything.
 * - DIP: Hardcodes direct `new` instantiations of database and mail services instead of interfaces.
 * 
 * Refactor this class into clean, decoupled, testable components!
 */
public class GodOrderService {

    public void processOrder(String customerEmail, double amount, String paymentType, String item) {
        // Validation
        if (customerEmail == null || !customerEmail.contains("@")) {
            throw new IllegalArgumentException("Invalid email");
        }
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }

        // Calculation with hardcoded discounts
        double finalAmount = amount;
        if (amount > 1000) {
            finalAmount = amount * 0.90; // 10% discount
        }

        // Hardcoded Payment Gateway Integration
        if ("CREDIT_CARD".equalsIgnoreCase(paymentType)) {
            System.out.println("Connecting to Stripe API... Charging $" + finalAmount);
        } else if ("PAYPAL".equalsIgnoreCase(paymentType)) {
            System.out.println("Redirecting to PayPal API... Charging $" + finalAmount);
        } else {
            throw new UnsupportedOperationException("Unknown payment type: " + paymentType);
        }

        // Hardcoded Database persistence
        System.out.println("INSERT INTO orders (email, item, amount) VALUES ('" + customerEmail + "', '" + item + "', " + finalAmount + ")");

        // Hardcoded Notification sending
        System.out.println("Connecting to SMTP server at smtp.gmail.com:587...");
        System.out.println("Sending confirmation email to " + customerEmail + " for item " + item);
    }
}
