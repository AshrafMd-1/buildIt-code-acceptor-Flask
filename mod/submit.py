from mod import script_variable
import json
from timeit import default_timer as timer


def submit_code(session, code, question, comp, course):
    validate_url = 'http://13.234.234.30:5000/validateSubmission'
    validate_headers = {
        'authorization': session.cookies['token'],
    }
    validate_payload = {
        "source_code": code,
        "language_id": script_variable.lang_code(comp),
        "stdin": "",
        "contestId": "",
        "courseId": course,
        "user": session.cookies['user'],
        "questionId": "IARE" + question}
    start = timer()
    res = session.post(validate_url, data=validate_payload, headers=validate_headers)
    result = json.loads(res.content)
    end = timer()
    return [end - start, result["score"], result["result"], ]
