{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "da6f0e97-153c-4dd9-b00f-0a949203f420",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2025-06-07 03:13:05--  https://raw.githubusercontent.com/alexeygrigorev/minsearch/refs/heads/main/minsearch.py\n",
      "Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.110.133, 185.199.109.133, ...\n",
      "Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 3832 (3.7K) [text/plain]\n",
      "Saving to: ‘minsearch.py’\n",
      "\n",
      "minsearch.py        100%[===================>]   3.74K  --.-KB/s    in 0s      \n",
      "\n",
      "2025-06-07 03:13:06 (40.7 MB/s) - ‘minsearch.py’ saved [3832/3832]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget https://raw.githubusercontent.com/alexeygrigorev/minsearch/refs/heads/main/minsearch.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eda75926-e415-49f6-8789-3fdeba2ae9fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import minsearch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "334908b5-250e-4389-8234-1c47e9dece24",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b411ca46-92b7-4a11-952f-70daeb45319d",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'documents.json'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mdocuments.json\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mrt\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f_in:\n\u001b[32m      2\u001b[39m     docs_raw = json.load(f_in)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~/.local/lib/python3.12/site-packages/IPython/core/interactiveshell.py:325\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    318\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    319\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    320\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    321\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    322\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    323\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m325\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'documents.json'"
     ]
    }
   ],
   "source": [
    "with open('documents.json', 'rt') as f_in:\n",
    "    docs_raw = json.load(f_in)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "99f6f946-6e7e-454f-839e-982150966d81",
   "metadata": {},
   "outputs": [],
   "source": [
    "import minsearch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "834be4de-1d4d-4059-b5c7-85587751d26f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fea24119-3a20-4910-b052-b85f6ad4899b",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'documents.json'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mdocuments.json\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mrt\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f_in:\n\u001b[32m      2\u001b[39m     docs_raw = json.load(f_in)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~/.local/lib/python3.12/site-packages/IPython/core/interactiveshell.py:325\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    318\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    319\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    320\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    321\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    322\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    323\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m325\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: 'documents.json'"
     ]
    }
   ],
   "source": [
    "with open('documents.json', 'rt') as f_in:\n",
    "    docs_raw = json.load(f_in)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2fc91365-9947-4021-8dff-dd8c15d99841",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('documents.json', 'rt') as f_in:\n",
    "    docs_raw = json.load(f_in)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "19b850ea-c2f2-4900-8fdc-60ff9b44a00b",
   "metadata": {},
   "outputs": [],
   "source": [
    "documents = []\n",
    "\n",
    "for course_dict in docs_raw:\n",
    "    for doc in course_dict['documents']:\n",
    "        doc['course'] = course_dict['course']\n",
    "        documents.append(doc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "19f3fca3-82b0-4299-987f-c94bfe70c736",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'text': \"The purpose of this document is to capture frequently asked technical questions\\nThe exact day and hour of the course will be 15th Jan 2024 at 17h00. The course will start with the first  “Office Hours'' live.1\\nSubscribe to course public Google Calendar (it works from Desktop only).\\nRegister before the course starts using this link.\\nJoin the course Telegram channel with announcements.\\nDon’t forget to register in DataTalks.Club's Slack and join the channel.\",\n",
       " 'section': 'General course-related questions',\n",
       " 'question': 'Course - When will the course start?',\n",
       " 'course': 'data-engineering-zoomcamp'}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "documents[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "dc1d88ec-df60-4183-912d-9f56b6c9efab",
   "metadata": {},
   "outputs": [],
   "source": [
    "index = minsearch.Index(\n",
    "    text_fields = [\"question\", \"text\", \"section\"],\n",
    "    keyword_fields=[\"course\"]\n",
    "                    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b60a9401-5a6b-4baa-8ad7-ed5b0c322795",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2886863330.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[17]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mSELECT * WHERE course = 'data-engineering-zoomcamp';\u001b[39m\n                   ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "SELECT * WHERE course = 'data-engineering-zoomcamp';"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1059b52a-50b9-407c-9f7b-b54b34d00c21",
   "metadata": {},
   "outputs": [],
   "source": [
    "q = 'the course has already started, can i still enroll?'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "224db23d-8cd2-4430-b7f5-b6565a6ec7d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<minsearch.Index at 0x7e54a0603e00>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "index.fit(documents)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "37873db3-4f7a-4bf8-bcc4-5c77ff7a6beb",
   "metadata": {},
   "outputs": [],
   "source": [
    "boost = {'question': 3.0, 'section': 0.5}\n",
    "\n",
    "results = index.search(\n",
    "    query=q,\n",
    "    filter_dict={'course': 'data-engineering-zoomcamp'},\n",
    "    boost_dict=boost,\n",
    "    num_results=5\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d4ad6c40-d616-4abe-9027-656472782069",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'text': \"Yes, even if you don't register, you're still eligible to submit the homeworks.\\nBe aware, however, that there will be deadlines for turning in the final projects. So don't leave everything for the last minute.\",\n",
       "  'section': 'General course-related questions',\n",
       "  'question': 'Course - Can I still join the course after the start date?',\n",
       "  'course': 'data-engineering-zoomcamp'},\n",
       " {'text': 'Yes, we will keep all the materials after the course finishes, so you can follow the course at your own pace after it finishes.\\nYou can also continue looking at the homeworks and continue preparing for the next cohort. I guess you can also start working on your final capstone project.',\n",
       "  'section': 'General course-related questions',\n",
       "  'question': 'Course - Can I follow the course after it finishes?',\n",
       "  'course': 'data-engineering-zoomcamp'},\n",
       " {'text': \"The purpose of this document is to capture frequently asked technical questions\\nThe exact day and hour of the course will be 15th Jan 2024 at 17h00. The course will start with the first  “Office Hours'' live.1\\nSubscribe to course public Google Calendar (it works from Desktop only).\\nRegister before the course starts using this link.\\nJoin the course Telegram channel with announcements.\\nDon’t forget to register in DataTalks.Club's Slack and join the channel.\",\n",
       "  'section': 'General course-related questions',\n",
       "  'question': 'Course - When will the course start?',\n",
       "  'course': 'data-engineering-zoomcamp'},\n",
       " {'text': 'You can start by installing and setting up all the dependencies and requirements:\\nGoogle cloud account\\nGoogle Cloud SDK\\nPython 3 (installed with Anaconda)\\nTerraform\\nGit\\nLook over the prerequisites and syllabus to see if you are comfortable with these subjects.',\n",
       "  'section': 'General course-related questions',\n",
       "  'question': 'Course - What can I do before the course starts?',\n",
       "  'course': 'data-engineering-zoomcamp'},\n",
       " {'text': 'Yes, the slack channel remains open and you can ask questions there. But always sDocker containers exit code w search the channel first and second, check the FAQ (this document), most likely all your questions are already answered here.\\nYou can also tag the bot @ZoomcampQABot to help you conduct the search, but don’t rely on its answers 100%, it is pretty good though.',\n",
       "  'section': 'General course-related questions',\n",
       "  'question': 'Course - Can I get support if I take the course in the self-paced mode?',\n",
       "  'course': 'data-engineering-zoomcamp'}]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e36778fb-df48-418e-8936-ba4c0a381ed9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from google import genai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "81d0e179-8325-464a-b9dd-427e2f5d6ca8",
   "metadata": {},
   "outputs": [],
   "source": [
    "client = genai.Client(api_key=\"enter your api\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "16ee3b06-3edb-4743-a77a-4b05aef4ba59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Okay. Do you have a question for me? I'm ready to help if you need information, want to brainstorm ideas, or just want to chat. Just let me know what you'd like to talk about.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "response = client.models.generate_content(\n",
    "    model=\"gemini-2.0-flash\", contents=\"q\"\n",
    ")\n",
    "print(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52417a88-21a2-4be6-be04-53f9f303492c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
