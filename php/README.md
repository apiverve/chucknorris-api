# Chuck Norris Jokes API - PHP Package

Chuck Norris Jokes delivers a random Chuck Norris joke on every request without requiring any query parameters. Each call returns plain joke text ready to display in bots, command-line interfaces, or entertainment feeds.

## Installation

Install via Composer:

```bash
composer require apiverve/chucknorris
```

## Getting Started

Get your API key at [APIVerve](https://apiverve.com)

### Basic Usage

```php
<?php

require_once 'vendor/autoload.php';

use APIVerve\Chucknorris\Client;

// Initialize the client
$client = new Client('YOUR_API_KEY');

// Make a request
$response = $client->execute();

// Print the response
print_r($response);
```


### Error Handling

```php
use APIVerve\Chucknorris\Client;
use APIVerve\Chucknorris\Exceptions\APIException;
use APIVerve\Chucknorris\Exceptions\ValidationException;

try {
    $response = $client->execute([]);
    print_r($response['data']);
} catch (ValidationException $e) {
    echo "Validation error: " . implode(', ', $e->getErrors());
} catch (APIException $e) {
    echo "API error: " . $e->getMessage();
    echo "Status code: " . $e->getStatusCode();
}
```

### Debug Mode

```php
// Enable debug logging
$client = new Client(
    apiKey: 'YOUR_API_KEY',
    debug: true
);
```

## Example Response

```json
{
  "status": "ok",
  "error": null,
  "data": {
    "joke": "The Mona Lisa Used To Smile, Then Chuck Norris Roundhouse Kicked It"
  }
}
```

## Requirements

- PHP 7.4 or higher
- Guzzle HTTP client

## Documentation

For more information, visit the [API Documentation](https://docs.apiverve.com/ref/chucknorris?utm_source=packagist&utm_medium=referral&utm_content=readme).

## Support

- Website: [https://apiverve.com/marketplace/chucknorris?utm_source=php&utm_medium=referral&utm_content=readme](https://apiverve.com/marketplace/chucknorris?utm_source=php&utm_medium=referral&utm_content=readme)
- Email: hello@apiverve.com

## License

This package is available under the [MIT License](LICENSE).
