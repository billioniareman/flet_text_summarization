def text_sumup(text):
    from transformers import pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    result=summarizer(text, max_length=100, min_length=50)

    list_to_dict=result[0]
    return list_to_dict['summary_text']