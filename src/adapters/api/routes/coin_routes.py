from fastapi import APIRouter, Depends, status, HTTPException

from src.adapters.api.auth import authenticate_user
from src.adapters.api.dependencies import get_coin_use_case
from src.domain.dtos.coin_dto import CoinRequestDto, CoinResponseDto
from src.domain.exceptions.coin_price_exception import CoinPriceNotFoundException
from src.domain.usecases.get_coin_price_usecase import GetCoinPriceUseCase

router = APIRouter()

@router.post(
    "/coin_infos",
    response_model=CoinResponseDto,
    status_code=status.HTTP_200_OK,
    tags=["Coin Information"],
    summary="Retrieve coin price information",
    description=(
        "This endpoint retrieves detailed information about the price of a coin "
        "based on the symbol provided."
    ),
)
async def get_coin_info(
    payload: CoinRequestDto,
    user: str = Depends(authenticate_user),
    use_case: GetCoinPriceUseCase = Depends(get_coin_use_case)
):  
    try:
        return await use_case.execute(payload.symbol)
    except CoinPriceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Price information for coin '{payload.symbol}' not found."
        )

