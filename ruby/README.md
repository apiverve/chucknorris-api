# Chuck Norris Jokes API - Ruby Gem

Chuck Norris Jokes delivers a random Chuck Norris joke on every request without requiring any query parameters. Each call returns plain joke text ready to display in bots, command-line interfaces, or entertainment feeds.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'apiverve_chucknorris'
```

And then execute:

```bash
$ bundle install
```

Or install it yourself as:

```bash
$ gem install apiverve_chucknorris
```

## Getting Started

Get your API key at [APIVerve](https://apiverve.com)

### Basic Usage

```ruby
require 'apiverve_chucknorris'

# Initialize the client
client = APIVerve::Chucknorris::Client.new(api_key: "YOUR_API_KEY")

# Make a request
response = client.execute

# Print the response
puts response
```


### Error Handling

```ruby
begin
  response = client.execute({  })
  puts response["data"]
rescue APIVerve::Chucknorris::ValidationError => e
  puts "Validation error: #{e.errors.join(', ')}"
rescue APIVerve::Chucknorris::APIError => e
  puts "API error: #{e.message}"
  puts "Status code: #{e.status_code}"
end
```

### Debug Mode

```ruby
# Enable debug logging
client = APIVerve::Chucknorris::Client.new(
  api_key: "YOUR_API_KEY",
  debug: true
)
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

## Documentation

For more information, visit the [API Documentation](https://docs.apiverve.com/ref/chucknorris?utm_source=rubygems&utm_medium=referral&utm_content=readme).

## Support

- Website: [https://apiverve.com/marketplace/chucknorris?utm_source=ruby&utm_medium=referral&utm_content=readme](https://apiverve.com/marketplace/chucknorris?utm_source=ruby&utm_medium=referral&utm_content=readme)
- Email: hello@apiverve.com

## License

This gem is available under the [MIT License](LICENSE).
