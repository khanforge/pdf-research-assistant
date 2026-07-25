import streamlit as st
from agentic_rag.assistant import ResearchAssistant
from ingestion.pipeline import IngestionPipeline
from pathlib import Path

def get_source_name(metadata: dict) -> str:
    """
    Return only the filename from a document source.
    """

    source = metadata.get("source", "Unknown")

    return Path(source).name

st.set_page_config(
    page_title = "Agentic PDF Research Assistant",
    page_icon = "📜",
    layout = "wide",
    initial_sidebar_state = "auto",
)

if "assistant" not in st.session_state:
    st.session_state.assistant = ResearchAssistant()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pipeline" not in st.session_state:
    st.session_state.pipeline = IngestionPipeline()

with st.sidebar:
    st.header("📂 Documents")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    # st.divider()

    if st.button("🗑 Reset Chat"):
        st.session_state.messages = []
        st.session_state.assistant = ResearchAssistant()
        st.rerun()

if uploaded_file:
    upload_dir = Path("data/uploads")
    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    pdf_path = upload_dir / uploaded_file.name

    with open(pdf_path, "wb") as f:
        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button("🚀 Process PDF"):

        with st.spinner(
            "Indexing document..."
        ):
            print(pdf_path)

            st.session_state.pipeline.ingest(
                pdf_path
            )

        st.success(
            "Document indexed successfully!"
        )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask something about your PDF...")

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.status(
        "Running Agent...", expanded=True
    ) as status:
        status.write("📝 Rewriting query...")
        status.write("🔍 Retrieving documents...")
        status.write("🤔 Reflecting on retrieved context...")
        status.write("✍️ Generating answer...")

        result = st.session_state.assistant.ask(question)

        status.update(
            label="✅ Agent Finished",
            state="complete"
        )

    answer = result.get("answer", "No answer generated!")

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.expander("🔍 Agent Trace"):

        st.write(
            "Original Question:",
            result["question"]
        )

        st.write(
            "Rewritten Query:",
            result.get(
                "rewritten_query",
                ""
            )
        )

        st.write(
            "Reflection:",
            result.get(
                "reflection",
                False
            )
        )

        st.write(
            "Retries:",
            result.get(
                "retry_count",
                0
            )
        )

    with st.expander("📚 Retrieved Documents"):

        for i, doc in enumerate(
            result["documents"],
            start=1
        ):

            st.markdown(
                f"### Chunk {i}"
            )

            st.write(
                doc.page_content[:500]
            )

            st.divider()

    with st.expander("📚 Sources", expanded=False):

        for i, doc in enumerate(result["documents"], start=1):

            filename = get_source_name(doc.metadata)

            page = doc.metadata.get("page", 0) + 1

            st.markdown(
                f"**{i}. {filename} — Page {page}**"
            )

            st.info(doc.page_content)

            st.divider()