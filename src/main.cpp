#include <stdio.h>
#include "pico/stdlib.h"
#include <iostream> // For std::cout, std::cin (though we'll use printf/getchar for pico)
#include <string>   // For std::string
#include <algorithm> // For std::transform for case-insensitive comparison

// Function to display the puzzle text
void display_puzzle(const std::string& puzzle_text) {
    printf("%s\n", puzzle_text.c_str());
}

// Function to get user input from the serial console
std::string get_user_input() {
    std::string user_input_str;
    char c;
    printf("Enter your answer: ");
    while (true) {
        c = getchar();
        if (c == '\n' || c == '\r') {
            // Echo the newline to the console for better user experience
            printf("\n"); 
            break;
        }
        if (c != PICO_ERROR_TIMEOUT) {
            // Echo the character back to the console
            putchar(c); 
            user_input_str += c;
        }
    }
    return user_input_str;
}

// Helper function for case-insensitive string comparison
bool iequals(const std::string& a, const std::string& b) {
    if (a.length() != b.length()) {
        return false;
    }
    return std::equal(a.begin(), a.end(), b.begin(),
                      [](char a_char, char b_char) {
                          return tolower(a_char) == tolower(b_char);
                      });
}

int main() {
    stdio_init_all(); // Initialize all available stdio types

    // Wait a bit for the serial console to connect
    // (Useful when auto-connecting and resetting the Pico)
    for (int i = 0; i < 5; ++i) {
        printf("Waiting for console... %d\n", 5 - i);
        sleep_ms(500);
    }
    printf("Console connected!\n");


    std::string riddle = "What has an eye, but cannot see?";
    std::string answer = "needle";

    display_puzzle(riddle);
    std::string user_answer = get_user_input();

    // Case-insensitive comparison
    if (iequals(user_answer, answer)) {
        printf("Correct!\n");
    } else {
        printf("Try again. Your answer was: %s\n", user_answer.c_str());
        printf("The correct answer is: %s\n", answer.c_str());
    }

    // Loop forever after one attempt
    while (true) {
        // You could add a sleep here if you want to reduce CPU usage
        // Or allow re-trying the puzzle.
        sleep_ms(1000); 
    }

    return 0; // Should not be reached
}
