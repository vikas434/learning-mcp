from typing import Any, Dict, List
import json
import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bits-course")

# BITS Second Year Course Data
Second_Year_Guide = [
    {
        "subjects": [
            {
                "subject": "CHE F211, Chemical process calculations",
                "content": [
                    "The course is based on the principles of mass balance.",
                    "You should be clear on the law of conservation of mass.",
                    "This course becomes boring as soon as it starts, but it can be tricky to apply the logic as they have been taught in the class during your exams.",
                    "Attend classes and tutorials regularly, you'll have a lot of tut tests in this subject, 6-7 spread through the semester so try and keep up with the classes.",
                    "Practice questions done during lectures and tutorials to solidify your concepts.",
                    "Examples from textbook, lecture material are the ideal resources to study.",
                    "Strict grading, try and score as many marks in the tut tests as the mid sems and compres are lengthy and tricky to solve.",
                    "Take inputs from the lecturer on how to do the assignments to score extra marks."
                ]
            },
            {
                "subject": "CHE F212, Fluid Mechanics",
                "content": [
                    "This course is the basic introduction to fluid mechanics, covering the fundamental and practical aspects of fluid flow.",
                    "It is an important technical subject which will be taken up during interviews if you opt for Core Chemical Sls.",
                    "Also, a prerequisite for Chemical Lab-l which will come up during your 3-1.",
                    "The recommended textbook (Fox, R.W. and A.T. McDonalds, Introduction to Fluid Mechanics (8th Ed.), John Wiley & Sons Inc., 2011.) is great, has good explanations for concepts and examples accompanying this.",
                    "Dr, Pratik N Sheth was my instructor and his classes can be a little slow at times but you are recommended to go to lectures because he gives out problems during lecture hours which helps you understand the concepts and also, ace the tutorial tests.",
                    "Lectures and tutorial hours are a must attend. There are 7 surprise tut tests out of which 6 are counted.",
                    "These are open/closed books which are announced during the tut hour.",
                    "It is easier to score for the tut tests as the aggregated average is generally low and you can score well above the average at the end of the semester.",
                    "Mid-sem and Compre have both open and closed book tests and for which I recommend to brush up the examples and basics, the questions for the closed book tests can be direct and concept based whereas, for the open book you have to be thorough with practice.",
                    "Grading is good, in a class of 120 students about 14 students got A grade.",
                    "Average + 6-8 helps you get a B-."
                ]
            },
            {
                "subject": "CHE F213, Chemical Engineering Thermodynamics",
                "content": [
                    "This course involves the application of the first and second laws of thermodynamics, basics that you've learned in Thermodynamics in your first year.",
                    "Applications of work, heat, reversible and irreversible processes. Equation of states, generalized correlation for the PVT behavior.",
                    "A lot of new and important concepts like the Maxwell relations, fluid property estimations, Gibbs-Duhem equation and Vapor Liquid Equilibria are introduced.",
                    "We had lectures as well as tutorial tests. The lectures are fast paced but don't rush through the syllabus.",
                    "The advantages of attending lectures is that it helps you cover most of the syllabus for the tutorial tests as you'll only have to practice examples given in the textbook.",
                    "Although most of the content taught in the lecture is straight out of the textbook, it takes time to understand the basic concepts which are important if you are looking for a Core job as this is one of the important subjects.",
                    "The recommended textbook (J. M. Smith,, H C Van Ness, M. M. Abbott and M. T. Swihart (Adapted by: B I Bhatt), Introduction to Chemical Engineering Thermodynamics (8th ed.), Tata McGraw Hill, special Indian Edition 2020.)is pretty much all you need to study.",
                    "I would suggest all the examples from each of the chapters to be solved as the tut test questions as well as the open book questions in mid sem and compre are pretty straight forward.",
                    "Mark the textbook well otherwise you'll be lost during open book exams.",
                    "Like in Fluid Mechanics, try attempting all the tut-tests as they push you well above average.",
                    "Open book marking is purely final answer based, so make sure to complete the questions in mid-sem and compres. Keep in handy all the values of gas constant for the closed book tests.",
                    "A.K. Pani is an amazing teacher and will value you if you are regular in his classes."
                ]
            },
            {
                "subject": "CHE F214, Engineering Chemistry",
                "content": [
                    "The course is about understanding the various developments in the field of water treatment, polymers, instrumental method of analysis, etc. The objective of the course is to study these areas in detail, and understand the important working principles of equipment involved.",
                    "To score good marks in all the evaluations please attend lectures.",
                    "The professor takes attendance very seriously and is partial towards people who attend classes.",
                    "A lot of important material is taught during tutorial hours, so make sure you attend those.",
                    "There are no surprise tests, all the tests will be announced beforehand.",
                    "The recommended book (Vairam SRamesh SEngineering Chemistry, Wiley India, 2011) is very extensive, and lectures only cover like 45% of the material which is expected of you during examinations.",
                    "There is a lot of material to learn because the course is completely closed book.",
                    "Be regular with the reading of the textbook to not pile up just before exams.",
                    "PYQs are important as they give an idea about important topics which you should focus on, like wastewater treatment is one of the most important topics.",
                    "Strict checking and grading. Each word in your answer sheet will be evaluated for its relevance.",
                    "To the point answers are expected. We also had an assignment which was evaluated on the basis of our knowledge of the topic and research work."
                ]
            },
            {
                "subject": "MATH F211, Mathematics-III",
                "content": [
                    "This course is the study of differential equations with the introduction to solving boundary value problems using various classical methods.",
                    "You have to have thorough knowledge of differential equations taught in calculus of +2.",
                    "Attending lectures of Prof. Krishnendra Shekhawat, as along with basic concepts he gives out a lot of problems to solve during lecture hours which will make it easier to understand.",
                    "Solve suggested questions from the textbook and pyqs to help understand as well as learn the concepts.",
                    "Make marked notes to make sure you don't waste your time skimming through the notes during open book exams.",
                    "It is a very high scoring subject and you need to really practice to know the type of questions asked and manage time efficiently during exams.",
                    "2 out of 3 tut tests are considered which again are very high scoring so try to remain above average at all times.",
                    "A grade was given on Av+ 75."
                ]
            },
            {
                "subject": "CHE F241, Heat Transfer",
                "content": [
                    "The course is about the steady and unsteady state conduction, convection and radiation. It starts off with the basics of heat transfer due to conduction and convection that we've already learnt in class 12. Then the level increases with the introduction to fins and unsteady state convection. And then there will be many dimensionless numbers which will be in use like reynolds, grashoffs, nusselts, and it can be a little confusing at times.",
                    "Lectures can keep you updated for the tut tests and you will understand how to solve the problems. The lectures are based on books and you will be solving a lot of questions to help with the concepts. There'll be 6 tut-tests out of which 4 will be considered and 2 assignments before mid sem and compre respectively",
                    "Understand the concepts using the recommended textbook (Holman, J.P., Bhattacharyya, S. (2011), \"Heat Transfer\", 10th Ed., Tata McGraw Hill Education Pvt Ltd, New Delhi.), quick revision through slides, before mid sem and compre take the assignments seriously, similar questions are asked. Solve the given examples for practice and the questions covered during lecture hours. Give all the tutorial tests to stay well above average and take the pressure off mid sem and compre.",
                    "Good grading depending on the class strength about 10 % people get A. This is an important subject if you want to study Transport Phenomenon and Computational Fluid Dynamics. The concepts will also be used in Chem Lab I in your 3-1.",
                    "Don't freak due to closed book tests as the questions asked are based on basic concepts taught in lectures. You don't have to learn the bigger formulas, just the easy ones and know how to correlate the concepts."
                ]
            },
            {
                "subject": "CHE F242, Numerical Methods for Chemical Engineering",
                "content": [
                    "This is the introduction to mathematical modeling and engineering problem solving. It will help students to use numerical techniques to solve allergic and differential equations. Learning numerical methods for differentiation, integration and curve fitting, which helps us solve various problems of Chemical engineering subjects.",
                    "This course is all about problem solving and practice. Questions done during lecture hour, tutorial hour and PYQs. Try learning MATLAB along with this subject to get hold of the software as it is very important for chemical engineering.",
                    "The textbook (Chapra, S. C. and R. P. Canale, Numerical Methods for Engineers, 7th Edition, McGraw Hill Education (India) Pvt. Ltd., New Delhi, 2015) has a lot of problems to practice, tutorial hours are important as there are many surprise tests.",
                    "In a class of about 120 students 11-13 students get an A grade.",
                    "There is a lot to remember for the closed book test so make sure you are in regular practice to not get confused between the concepts."
                ]
            },
            {
                "subject": "CHE F243, Material Science",
                "content": [
                    "Introduction to various materials for engineering and their significant properties. You learn about metals, ceramics, polymers and composites. Corrosion of materials and the evolution of materials.",
                    "The book is easy to understand but the questions asked are seldom from the book. Questions practiced during tutorial hours are important and direct questions are asked in the exams. Attending lectures is completely up to you.",
                    "PYQs are important as the tests are mostly numerical with little to no theory asked.",
                    "Strict grading for tests and assignments. You won't be allowed in the class if you are 5+ mins late."
                ]
            },
            {
                "subject": "CHE F244, Separation Process I",
                "content": [
                    "The most interesting subjects of 2-2. All you have to do is go to lectures, make notes and that's it. It is about molecular diffusion in fluids, mass transfer, mass transfer coefficient and concepts involved in adsorption, stripping, distillation and liquid-liquid extraction. You'll learn problem solving in the lectures and all the concepts are so well taught.",
                    "To study this subject all you need are the notes and understanding the art of graphical problem solving which will be taught during lecture hours.",
                    "Practice problems from assignments and PYQs, direct questions are asked in tut tests and mid sem compres.",
                    "Important prerequisites for Chemical Lab I and Separation Process II. The grading is linenet."
                ]
            },
            {
                "subject": "ECON F211, Principles of Economics",
                "content": [
                    "PoE is a foundation course that introduces us to the field of Economics and Finance. We are taught all the basics economics, micro and macro. It is an important course if you are thinking of pursuing a Finance Minor.",
                    "PYQs is the best way to study the subject as the questions asked during tut tests and mid sem compres are very similar and you just need to know the methodology of solving certain problems.",
                    "The recommended textbook is amazing, you get to learn everything through examples. If you find yourself not attending classes, I suggest you diligently read the textbook and keep up with the syllabus in order to not fall behind.",
                    "About 700-800 students take up this course so it has a better range for grading but a lot of students tend to take lite and since it's a very scoring subject averages are very high so don't fall below the average line because it awards you a C grade."
                ]
            }
        ]
    }
]

def search_subjects_by_keyword(keyword: str) -> List[Dict[str, Any]]:
    """Search for subjects containing a specific keyword."""
    results = []
    keyword_lower = keyword.lower()
    
    for section in Second_Year_Guide:
        for subject in section.get("subjects", []):
            subject_name = subject.get("subject", "").lower()
            content = " ".join(subject.get("content", [])).lower()
            
            if keyword_lower in subject_name or keyword_lower in content:
                results.append({
                    "subject": subject.get("subject"),
                    "content": subject.get("content")
                })
    
    return results

def get_all_subjects() -> List[str]:
    """Get a list of all available subjects."""
    subjects = []
    for section in Second_Year_Guide:
        for subject in section.get("subjects", []):
            subjects.append(subject.get("subject"))
    return subjects

@mcp.tool()
async def get_subject_details(subject_name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific BITS 2nd year subject.
    
    Args:
        subject_name: The name or code of the subject (e.g., "CHE F211", "Fluid Mechanics", "Mathematics-III")
    
    Returns:
        Dictionary containing subject details including content and study tips
    """
    subject_name_lower = subject_name.lower()
    
    for section in Second_Year_Guide:
        for subject in section.get("subjects", []):
            subject_full = subject.get("subject", "")
            if (subject_name_lower in subject_full.lower() or 
                any(subject_name_lower in part.lower() for part in subject_full.split(", "))):
                
                return {
                    "subject": subject_full,
                    "content": subject.get("content", []),
                    "total_points": len(subject.get("content", [])),
                    "formatted_content": "\n• " + "\n• ".join(subject.get("content", []))
                }
    
    return {
        "error": f"Subject '{subject_name}' not found.",
        "available_subjects": get_all_subjects()[:5],  # Show first 5 as examples
        "suggestion": "Try searching with subject code (e.g., 'CHE F211') or partial name (e.g., 'Fluid Mechanics')"
    }

@mcp.tool()
async def search_course_topics(topic: str) -> Dict[str, Any]:
    """
    Search for courses related to a specific topic or keyword.
    
    Args:
        topic: The topic to search for (e.g., "thermodynamics", "mathematics", "grading", "textbook")
    
    Returns:
        Dictionary containing matching subjects and relevant content
    """
    results = search_subjects_by_keyword(topic)
    
    if not results:
        return {
            "message": f"No courses found related to '{topic}'",
            "suggestion": "Try searching for terms like: thermodynamics, mathematics, chemistry, economics, heat transfer, fluid mechanics"
        }
    
    formatted_results = []
    for result in results:
        # Find relevant content lines that contain the topic
        relevant_content = [
            line for line in result["content"] 
            if topic.lower() in line.lower()
        ]
        
        formatted_results.append({
            "subject": result["subject"],
            "relevant_points": relevant_content[:3],  # Show top 3 relevant points
            "total_content_points": len(result["content"])
        })
    
    return {
        "topic_searched": topic,
        "matching_courses": len(formatted_results),
        "results": formatted_results
    }

@mcp.tool()
async def get_study_tips(subject_name: str = "") -> Dict[str, Any]:
    """
    Get study tips and recommendations for BITS 2nd year courses.
    
    Args:
        subject_name: Optional specific subject name. If not provided, returns general tips for all subjects.
    
    Returns:
        Dictionary containing study tips, grading information, and recommendations
    """
    if subject_name:
        # Get tips for specific subject
        subject_details = await get_subject_details(subject_name)
        if "error" in subject_details:
            return subject_details
        
        content = subject_details["content"]
        
        # Extract study tips, grading info, and recommendations
        study_tips = [line for line in content if any(keyword in line.lower() for keyword in 
                     ["attend", "practice", "study", "solve", "read", "learn", "understand"])]
        
        grading_info = [line for line in content if any(keyword in line.lower() for keyword in 
                       ["grading", "grade", "scoring", "marks", "average"])]
        
        textbook_info = [line for line in content if any(keyword in line.lower() for keyword in 
                        ["textbook", "book", "recommended"])]
        
        return {
            "subject": subject_details["subject"],
            "study_tips": study_tips,
            "grading_information": grading_info,
            "textbook_recommendations": textbook_info
        }
    else:
        # General tips across all subjects
        all_subjects = get_all_subjects()
        general_tips = {
            "attendance": "Most courses emphasize regular attendance for lectures and tutorials",
            "practice": "Solve PYQs (Previous Year Questions) and tutorial problems regularly",
            "textbooks": "Follow recommended textbooks and mark important formulas for open book exams",
            "tutorial_tests": "Tutorial tests are crucial for maintaining good averages",
            "time_management": "Start preparation early, don't pile up material before exams"
        }
        
        return {
            "total_subjects": len(all_subjects),
            "general_study_tips": general_tips,
            "available_subjects": all_subjects
        }

@mcp.tool()
async def list_all_subjects() -> Dict[str, Any]:
    """
    Get a complete list of all BITS 2nd year subjects available in the database.
    
    Returns:
        Dictionary containing all subject names organized by category
    """
    all_subjects = get_all_subjects()
    
    # Categorize subjects
    che_subjects = [s for s in all_subjects if s.startswith("CHE")]
    math_subjects = [s for s in all_subjects if s.startswith("MATH")]
    econ_subjects = [s for s in all_subjects if s.startswith("ECON")]
    other_subjects = [s for s in all_subjects if not any(s.startswith(prefix) for prefix in ["CHE", "MATH", "ECON"])]
    
    return {
        "total_subjects": len(all_subjects),
        "chemical_engineering": che_subjects,
        "mathematics": math_subjects,
        "economics": econ_subjects,
        "other_subjects": other_subjects,
        "all_subjects": all_subjects
    }

if __name__ == "__main__":
    # Run as SSE server
    mcp.run(transport="sse")
