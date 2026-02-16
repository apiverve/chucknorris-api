# Chuck Norris Jokes API - Dart/Flutter Client

Chuck Norris Jokes is a simple tool for getting Chuck Norris jokes. It returns a random Chuck Norris joke.

[![pub package](https://img.shields.io/pub/v/apiverve_chucknorris.svg)](https://pub.dev/packages/apiverve_chucknorris)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the Dart/Flutter client for the [Chuck Norris Jokes API](https://apiverve.com/marketplace/chucknorris?utm_source=dart&utm_medium=readme).

## Installation

Add this to your `pubspec.yaml`:

```yaml
dependencies:
  apiverve_chucknorris: ^1.1.14
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
    "joke": "Some Say That Chuck Has The Ability To Cencor All Who Mock Him. Wrong! So To Prove A Point, Chuck You're A[[this Comment Has Been Removed]}"
  }
}
```

## API Reference

- **API Home:** [Chuck Norris Jokes API](https://apiverve.com/marketplace/chucknorris?utm_source=dart&utm_medium=readme)
- **Documentation:** [docs.apiverve.com/ref/chucknorris](https://docs.apiverve.com/ref/chucknorris?utm_source=dart&utm_medium=readme)

## Authentication

All requests require an API key. Get yours at [apiverve.com](https://apiverve.com?utm_source=dart&utm_medium=readme).

## License

MIT License - see [LICENSE](LICENSE) for details.

---

Built with Dart for [APIVerve](https://apiverve.com?utm_source=dart&utm_medium=readme)
