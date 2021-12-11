import grpc

from recommendations.recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations.recommendations_pb2_grpc import RecommendationsStub

def app():
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)
    request = RecommendationRequest(
        user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
    )

if __name__ == '__main__':
    app()