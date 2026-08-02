// Nearest Multiple
// Given two integers, round the first to the nearest multiple of the second.

// Tests:
// Waiting:1. roundToNearestMultiple(5, 3) should return 6.
// Waiting:2. roundToNearestMultiple(17, 4) should return 16.
// Waiting:3. roundToNearestMultiple(43, 5) should return 45.
// Waiting:4. roundToNearestMultiple(38, 11) should return 33.
// Waiting:5. roundToNearestMultiple(93, 12) should return 96.

function roundToNearestMultiple(num, multiple) {

    const remainder = num % multiple;

    if (remainder < multiple / 2) {
        return num - remainder;
    } else {
        return num + multiple - remainder;
    }
}