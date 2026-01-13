import string

def analyze_text(input_file, output_file):
    try:
        # Using context manager 'with' to ensure file closes automatically
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        total_lines = len(lines)
        word_counts = {}
        total_words = 0

        # Processing the text
        for line in lines:
            # Remove punctuation and convert to lowercase
            clean_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = clean_line.split()
            
            total_words += len(words)
            
            # Count frequency
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

        # Writing results to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Total lines: {total_lines}\n")
            f.write(f"Total words: {total_words}\n")
            f.write("Word Frequency:\n")
            for word, count in word_counts.items():
                f.write(f"{word}: {count}\n")
        
        print(f"Analysis complete. Check {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")

# Execution
if __name__ == "__main__":
    analyze_text("text.txt", "analysis.txt")