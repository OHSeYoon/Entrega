// lib/text_box.dart
import 'package:flutter/material.dart';

class TextBox extends StatelessWidget {
  final TextEditingController controller;
  final String hintText;
  final EdgeInsetsGeometry padding;
  final Color hintColor;
  final TextStyle textStyle;
  final double width;
  final double height;
  final TextAlign textAlign;
  final TextInputType inputType;
  final int? maxLength;
  final ValueChanged<String>? onChanged;

  const TextBox({
    Key? key,
    required this.controller,
    required this.hintText,
    this.padding = const EdgeInsets.all(8.0),
    this.hintColor = Colors.grey,
    this.textStyle = const TextStyle(fontSize: 16),
    this.width = 500, 
    this.height = 50,
    this.textAlign = TextAlign.start,
    this.inputType = TextInputType.text,
    this.maxLength,
    this.onChanged,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: padding,
      child: SizedBox(
         width: width,
         height: height,
         child: TextField(
          controller: controller,
          style: textStyle,
          textAlign: textAlign,
          keyboardType: inputType,
          maxLength: maxLength,
          onChanged: onChanged,
          decoration: InputDecoration(
            border: OutlineInputBorder(),
            hintText: hintText,
            hintStyle: TextStyle(color: hintColor),
          ),
        ),
      ),
    );
  }
}
