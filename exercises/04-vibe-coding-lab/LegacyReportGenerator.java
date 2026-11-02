package com.journey.exercises.vibecoding;

import java.util.List;

/**
 * Exercise EX-04-3: Legacy Spaghetti Code
 * 
 * Step 1: Write JUnit 5 Characterization Tests to lock down current behavior.
 * Step 2: Use an AI assistant to refactor into clean Single Responsibility classes.
 * Step 3: Ensure all tests still pass!
 */
public class LegacyReportGenerator {

    public String generateInvoiceSummary(String customerType, List<Double> amounts, boolean isVip, String currency) {
        if (amounts == null || amounts.isEmpty()) {
            return "EMPTY_INVOICE";
        }

        double total = 0.0;
        int count = 0;
        for (Double amt : amounts) {
            if (amt != null && amt > 0) {
                total += amt;
                count++;
            }
        }

        // Apply discount logic
        double discount = 0.0;
        if ("ENTERPRISE".equalsIgnoreCase(customerType)) {
            discount = total * 0.15;
        } else if ("RETAIL".equalsIgnoreCase(customerType)) {
            if (total > 500) {
                discount = total * 0.05;
            }
        }

        if (isVip) {
            discount += total * 0.05;
        }

        double finalTotal = total - discount;
        double tax = finalTotal * 0.09; // 9% tax
        double payable = finalTotal + tax;

        StringBuilder sb = new StringBuilder();
        sb.append("=== INVOICE ===").append("\n");
        sb.append("Customer: ").append(customerType).append("\n");
        sb.append("Items: ").append(count).append("\n");
        sb.append(String.format("Subtotal: %.2f %s\n", total, currency));
        sb.append(String.format("Discount: %.2f %s\n", discount, currency));
        sb.append(String.format("Tax: %.2f %s\n", tax, currency));
        sb.append(String.format("Total Payable: %.2f %s\n", payable, currency));
        sb.append("===============");

        return sb.toString();
    }
}
