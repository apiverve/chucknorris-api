# Chuck Norris Jokes API - Dart/Flutter Client

Chuck Norris Jokes delivers a random Chuck Norris joke on every request without requiring any query parameters. Each call returns plain joke text ready to display in bots, command-line interfaces, or entertainment feeds.

[![pub package](https://img.shields.io/pub/v/apiverve_chucknorris.svg)](https://pub.dev/packages/apiverve_chucknorris)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the Dart/Flutter client for the [Chuck Norris Jokes API](https://apiverve.com/marketplace/chucknorris?utm_source=dart&utm_medium=referral&utm_content=readme).

## Installation

Add this to your `pubspec.yaml`:

```yaml
dependencies:
  apiverve_chucknorris: ^1.2.3
```

Then run:

```bash
dart pub get
# or for Flutter
flutter pub get
```

## Usage

```dart
import 'package:apiverve_chucknorris/apiverve_chucknorris.dart';

void main() async {
  final client = ChucknorrisClient('YOUR_API_KEY');

  try {
    final response = await client.execute();
    
    print('Status: ${response.status}');
    print('Data: ${response.data}');
  } catch (e) {
    print('Error: $e');
  }
}
```

## Response

```json
{
  "status": "ok",
  "error": null,
  "data": {
    "joke": "The Mona Lisa Used To Smile, Then Chuck Norris Roundhouse Kicked It"
  }
}
```

## API Reference

- **API Home:** [Chuck Norris Jokes API](https://apiverve.com/marketplace/chucknorris?utm_source=dart&utm_medium=referral&utm_content=readme)
- **Documentation:** [docs.apiverve.com/ref/chucknorris](https://docs.apiverve.com/ref/chucknorris?utm_source=dart&utm_medium=referral&utm_content=readme)

## Authentication

All requests require an API key. Get yours at [apiverve.com](https://apiverve.com?utm_source=dart&utm_medium=referral&utm_content=readme).

## License

MIT License - see [LICENSE](LICENSE) for details.

---

Built with Dart for [APIVerve](https://apiverve.com?utm_source=dart&utm_medium=referral&utm_content=readme)
