import streamlit as st
from pathlib import Path
import shutil
from collections import Counter
st.set_page_config(
    page_title="File Organizer",
    page_icon="📁",
    layout="wide"
)

FILE_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".svg", ".webp", ".ico", ".tiff"
    },

    "Documents": {
        ".pdf", ".doc", ".docx", ".txt",
        ".rtf", ".odt"
    },

    "Spreadsheets": {
        ".xls", ".xlsx", ".csv", ".ods"
    },

    "Presentations": {
        ".ppt", ".pptx", ".odp"
    },

    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm"
    },

    "Audio": {
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".m4a"
    },

    "Archives": {
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2"
    },

    "Code": {
        ".py", ".java", ".c", ".cpp",
        ".js", ".jsx", ".ts", ".tsx",
        ".html", ".css", ".sql",
        ".php", ".json", ".xml"
    }
}

def get_category(file_path):
    """Return the category of a file based on its extension."""

    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """
    Generate a unique filename if a file with the same
    name already exists.
    """

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def scan_folder(folder):
    """Scan the selected folder and return files."""

    files = []

    try:
        for item in folder.iterdir():

            # Ignore directories
            if not item.is_file():
                continue

            files.append(item)

    except PermissionError:
        st.error("Permission denied while reading this folder.")

    return files


def organize_files(folder, files):
    """Move files into category folders."""

    results = []

    for file in files:

        category = get_category(file)

        destination_folder = folder / category
        destination_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        destination = destination_folder / file.name

        # Handle duplicate filenames
        destination = get_unique_path(destination)

        try:
            shutil.move(str(file), str(destination))

            results.append({
                "file": file.name,
                "category": category,
                "status": "Moved",
                "destination": str(destination)
            })

        except Exception as error:

            results.append({
                "file": file.name,
                "category": category,
                "status": f"Error: {error}",
                "destination": "-"
            })

    return results

st.title("📁 Smart File Organizer")

st.markdown(
    """
    ### Organize your files automatically using Python

    This application scans a folder and organizes files into
    category-based folders according to their file extensions.
    """
)

st.divider()

st.sidebar.header("⚙️ Organizer Settings")

folder_path = st.sidebar.text_input(
    "Enter folder path",
    placeholder=r"C:\Users\YourName\Downloads"
)

st.sidebar.markdown("---")

st.sidebar.subheader("Supported Categories")

for category in FILE_CATEGORIES:
    st.sidebar.write(f"📂 {category}")

st.sidebar.write("📂 Others")

if not folder_path:

    st.info(
        "👈 Enter the folder path in the sidebar to begin."
    )

else:

    folder = Path(folder_path)

    if not folder.exists():

        st.error(
            "❌ The specified folder does not exist."
        )

    elif not folder.is_dir():

        st.error(
            "❌ The specified path is not a folder."
        )

    else:

        st.success(
            f"📁 Selected folder: `{folder}`"
        )
        if st.button(
            "🔍 Scan Folder",
            type="primary",
            use_container_width=True
        ):

            files = scan_folder(folder)

            st.session_state["files"] = files

            if not files:

                st.warning(
                    "No files were found in this folder."
                )

            else:

                st.success(
                    f"Found {len(files)} file(s)."
                )

        if "files" in st.session_state:

            files = st.session_state["files"]

            if files:

                st.subheader("📋 Files Found")

                file_data = []

                category_counter = Counter()

                for file in files:

                    category = get_category(file)

                    category_counter[category] += 1

                    file_data.append({
                        "File Name": file.name,
                        "Extension": file.suffix.lower()
                        if file.suffix else "No extension",
                        "Category": category,
                        "Size (KB)": round(
                            file.stat().st_size / 1024,
                            2
                        )
                    })

                st.dataframe(
                    file_data,
                    use_container_width=True,
                    hide_index=True
                )

                st.subheader("📊 Organization Summary")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "Total Files",
                    len(files)
                )

                col2.metric(
                    "Images",
                    category_counter["Images"]
                )

                col3.metric(
                    "Documents",
                    category_counter["Documents"]
                )

                col4.metric(
                    "Other Files",
                    category_counter["Others"]
                )

                st.markdown("---")
                st.subheader("📂 Category Breakdown")

                for category, count in sorted(
                    category_counter.items()
                ):

                    st.write(
                        f"**{category}:** {count} file(s)"
                    )

                st.markdown("---")
                st.warning(
                    "⚠️ This operation will move the files "
                    "into category folders."
                )

                if st.button(
                    "🚀 Organize Files",
                    type="primary",
                    use_container_width=True
                ):

                    with st.spinner(
                        "Organizing files..."
                    ):

                        results = organize_files(
                            folder,
                            files
                        )

                    st.session_state["results"] = results

                    st.success(
                        "✅ File organization completed!"
                    )

                if "results" in st.session_state:

                    results = st.session_state["results"]

                    st.subheader(
                        "📑 Organization Results"
                    )

                    result_data = []

                    for result in results:

                        result_data.append({
                            "File": result["file"],
                            "Category": result["category"],
                            "Status": result["status"],
                            "Destination": result["destination"]
                        })

                    st.dataframe(
                        result_data,
                        use_container_width=True,
                        hide_index=True
                    )

                    moved_count = sum(
                        1
                        for result in results
                        if result["status"] == "Moved"
                    )

                    st.metric(
                        "Successfully Organized",
                        moved_count
                    )

st.divider()

st.caption(
    "Python Programming Track | Task 22 | "
    "File Organizer"
)