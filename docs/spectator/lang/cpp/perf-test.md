# Performance

## Test Script

Test maximum single-threaded throughput for two minutes.

```cpp
#include <registry.h>
#include <chrono>
#include <iostream>
#include <iomanip>
#include <unordered_map>
#include <string>


int main()
{
    Logger::info("Starting UDP performance test...");

    //auto r = Registry(Config(WriterConfig(WriterTypes::UDP)));
    auto r = Registry(Config(WriterConfig(WriterTypes::Unix)));

    std::unordered_map<std::string, std::string>  tags = { {"location", "udp"}, {"version", "correct-horse-battery-staple"}};

    // Set maximum duration to 2 minutes
    constexpr int max_duration_seconds = 2 * 60;

    // Track iterations and timing
    unsigned long long iterations = 0;
    auto start_time = std::chrono::steady_clock::now();

    // Helper function to get elapsed time in seconds
    auto elapsed = [&start_time]() -> double {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration<double>(now - start_time).count();
    };

    while (true)
    {
        r.CreateCounter("udp_test_counter", tags).Increment();
        iterations++;

        if (iterations % 500000 == 0)
        {
            if (elapsed() > max_duration_seconds)
            {
                break;
            }
        }
    }

    double total_elapsed = elapsed();
    double rate_per_second = iterations / total_elapsed;

    Logger::info("Iterations completed: {}", iterations);
    Logger::info("Total elapsed time: {:.2f} seconds", total_elapsed);
    Logger::info("Rate: {:.2f} iterations/second", rate_per_second);
    return 0;
}
```

## Results

See [Usage > Performance](usage.md#performance).
