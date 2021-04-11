namespace QuantumSolvers {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;

    operation GenerateRandomBit() : Result {
        // Allocate a qubit
        use q = Qubit();
        // Put the qubit into superposition
        H(q);
        // It now has a 50% chance of being measured a One of Zero.
        // Measure the qubit value
        return M(q);
    }

    operation RandomNumberInRange(min: Int, max : Int, avoid : Int) : Int {
        // Create a variable to hold the output
        mutable output = 0;

        // Walk through the required bits to fulfill the max value requirement
        repeat {
            mutable bits = new Result[0];
            for idxBit in 1..BitSizeI(max) {
                set bits += [GenerateRandomBit()];
                }
            set output = ResultArrayAsInt(bits);
        }
        until (output <= max and output >= min and output != avoid);
        return output;
    }
}

