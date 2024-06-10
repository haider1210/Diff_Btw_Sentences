def generate_html_comparison(self, sentences1, sentences2):
    differ = difflib.HtmlDiff(tabsize=2, wrapcolumn=40)
    sentences1_lines = sentences1.splitlines()
    sentences2_lines = sentences2.splitlines()
    
    html_diff = differ.make_file(sentences1_lines, sentences2_lines, context=True, numlines=0)
    
    # Adding CSS to handle word wrap and set a maximum width
    wrapped_html_diff = re.sub(
        r'<style type="text/css">',
        '<style type="text/css"> .diff { white-space: pre-wrap; max-width: 50%; } ',
        html_diff
    )
    
    return wrapped_html_diff
