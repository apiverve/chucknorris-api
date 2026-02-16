/// Response models for the Chuck Norris Jokes API.

/// API Response wrapper.
class ChucknorrisResponse {
  final String status;
  final dynamic error;
  final ChucknorrisData? data;

  ChucknorrisResponse({
    required this.status,
    this.error,
    this.data,
  });

  factory ChucknorrisResponse.fromJson(Map<String, dynamic> json) => ChucknorrisResponse(
    status: json['status'] as String? ?? '',
    error: json['error'],
    data: json['data'] != null ? ChucknorrisData.fromJson(json['data']) : null,
  );

  Map<String, dynamic> toJson() => {
    'status': status,
    if (error != null) 'error': error,
    if (data != null) 'data': data,
  };
}

/// Response data for the Chuck Norris Jokes API.

class ChucknorrisData {
  String? joke;

  ChucknorrisData({
    this.joke,
  });

  factory ChucknorrisData.fromJson(Map<String, dynamic> json) => ChucknorrisData(
      joke: json['joke'],
    );
}
