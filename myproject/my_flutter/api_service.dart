import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> fetchHelloWorld() async {
  final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/hello/'));

  if (response.statusCode == 200) {
    var data = jsonDecode(response.body);
    print(data['message']); 
  } else {
    throw Exception('Failed to load data');
  }
}