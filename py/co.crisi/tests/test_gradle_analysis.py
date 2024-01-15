import gradle_analysis

def test_path_exists():
    # Given 
    path = 'C:\\Users\\cristian.sanchezp\\Documents\\project\\personal\\load-hours'

    #When 
    java_version = gradle_analysis.analyze_java_version(path)

    # then 
    assert java_version is not None
